import { useCallback, useEffect, useRef, useState } from 'react';
import PhotoCard from '../components/PhotoCard';

const PHOTOS_PER_PAGE = 24;

const PhotosPage = () => {
  const [photos, setPhotos] = useState([]);
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const observerRef = useRef(null);
  const sentinelRef = useRef(null);
  const fetchedPagesRef = useRef(new Set());
  const isFetchingRef = useRef(false);

  const fetchPhotos = useCallback(async (pageToLoad) => {
    if (isFetchingRef.current || fetchedPagesRef.current.has(pageToLoad) || !hasMore) {
      return;
    }

    fetchedPagesRef.current.add(pageToLoad);
    isFetchingRef.current = true;
    setLoading(true);
    setError(null);

    try {
      const response = await fetch(
        `https://picsum.photos/v2/list?page=${pageToLoad}&limit=${PHOTOS_PER_PAGE}`,
      );

      if (!response.ok) {
        throw new Error(`Failed to fetch photos (status ${response.status}).`);
      }

      const data = await response.json();

      if (data.length === 0) {
        setHasMore(false);
        return;
      }

      setPhotos((prev) => {
        const existingIds = new Set(prev.map((item) => item.id));
        const filtered = data.filter((item) => !existingIds.has(item.id));
        return filtered.length > 0 ? [...prev, ...filtered] : prev;
      });
    } catch (err) {
      fetchedPagesRef.current.delete(pageToLoad);
      setError(err.message || 'Unable to load photos. Please try again.');
    } finally {
      isFetchingRef.current = false;
      setLoading(false);
    }
  }, [hasMore]);

  useEffect(() => {
    fetchPhotos(page);
  }, [page, fetchPhotos]);

  const loadNextPage = useCallback(() => {
    if (!hasMore || isFetchingRef.current) {
      return;
    }
    setPage((prev) => prev + 1);
  }, [hasMore]);

  useEffect(() => {
    const sentinel = sentinelRef.current;
    if (!sentinel) {
      return undefined;
    }

    if (observerRef.current) {
      observerRef.current.disconnect();
    }

    observerRef.current = new IntersectionObserver(
      (entries) => {
        const firstEntry = entries[0];
        if (firstEntry?.isIntersecting) {
          loadNextPage();
        }
      },
      { root: null, rootMargin: '200px', threshold: 0 },
    );

    observerRef.current.observe(sentinel);

    return () => {
      observerRef.current?.disconnect();
    };
  }, [loadNextPage]);

  const handleRetry = () => {
    if (isFetchingRef.current) {
      return;
    }
    fetchPhotos(page);
  };

  return (
    <div className="content-wrapper">
      <div className="container py-4">
        <header className="mb-4 text-center">
          <h1 className="h2 fw-semibold">Lorem Picsum Gallery</h1>
          <p className="text-muted mb-0">
            Browse a curated feed of freely usable photos. Scroll for more and tap any image to dive
            into the details.
          </p>
        </header>

        {error && (
          <div className="alert alert-danger d-flex justify-content-between align-items-center" role="alert">
            <span>{error}</span>
            <button
              type="button"
              className="btn btn-sm btn-light"
              onClick={handleRetry}
              disabled={loading}
            >
              Retry
            </button>
          </div>
        )}

        <div className="row g-4">
          {photos.map((photo) => (
            <div className="col-12 col-sm-6 col-lg-4" key={photo.id}>
              <PhotoCard photo={photo} />
            </div>
          ))}
        </div>

        {!loading && photos.length === 0 && !error && (
          <div className="text-center text-muted py-5">No photos yet. Please try again shortly.</div>
        )}

        <div ref={sentinelRef} className="py-3" aria-hidden="true" />

        {loading && (
          <div className="d-flex justify-content-center py-4">
            <div className="spinner-border text-secondary" role="status" aria-label="Loading photos" />
          </div>
        )}

        {!hasMore && photos.length > 0 && (
          <div className="text-center py-4 end-of-list">You&apos;ve reached the end of the gallery.</div>
        )}
      </div>
    </div>
  );
};

export default PhotosPage;
