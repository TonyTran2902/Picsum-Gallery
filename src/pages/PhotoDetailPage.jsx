import { useEffect, useState } from 'react';
import { Link, useParams } from 'react-router-dom';

const PhotoDetailPage = () => {
  const { id } = useParams();
  const [photo, setPhoto] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let isMounted = true;
    const controller = new AbortController();

    const fetchPhotoDetails = async () => {
      setLoading(true);
      setError(null);

      try {
        const response = await fetch(`https://picsum.photos/id/${id}/info`, {
          signal: controller.signal,
        });

        if (!response.ok) {
          throw new Error(`Failed to fetch photo details (status ${response.status}).`);
        }

        const data = await response.json();

        if (isMounted) {
          setPhoto(data);
        }
      } catch (err) {
        if (err.name === 'AbortError') {
          return;
        }
        if (isMounted) {
          setError(err.message || 'Unable to load photo details. Please try again later.');
        }
      } finally {
        if (isMounted) {
          setLoading(false);
        }
      }
    };

    fetchPhotoDetails();

    return () => {
      isMounted = false;
      controller.abort();
    };
  }, [id]);

  const title = photo?.author ? `Captured by ${photo.author}` : `Photo #${id}`;
  const description =
    'This image is sourced from the Lorem Picsum public API. Use it freely in your prototypes and designs.';

  return (
    <div className="content-wrapper">
      <div className="container py-4">
        <nav className="mb-3">
          <Link to="/photos" className="btn btn-outline-secondary btn-sm">
            ← Back to gallery
          </Link>
        </nav>

        {loading && (
          <div className="d-flex justify-content-center py-5">
            <div className="spinner-border text-secondary" role="status" aria-label="Loading photo" />
          </div>
        )}

        {error && (
          <div className="alert alert-danger" role="alert">
            {error}
          </div>
        )}

        {!loading && !error && photo && (
          <div className="card shadow-sm">
            <div className="card-body">
              <h1 className="h4 fw-semibold mb-3">{title}</h1>
              <div className="mb-4 text-muted">
                <dl className="row mb-0">
                  <dt className="col-sm-3">Author</dt>
                  <dd className="col-sm-9">{photo.author || 'Unknown'}</dd>
                  <dt className="col-sm-3">Original Size</dt>
                  <dd className="col-sm-9">
                    {photo.width} × {photo.height}
                  </dd>
                  <dt className="col-sm-3">Source</dt>
                  <dd className="col-sm-9">
                    <a href={photo.url} target="_blank" rel="noreferrer">
                      View on Lorem Picsum
                    </a>
                  </dd>
                </dl>
              </div>

              <p className="text-muted">{description}</p>

              <div className="text-center">
                <img
                  src={photo.download_url}
                  alt={`Full size photo ${id} by ${photo.author}`}
                  className="img-fluid rounded photo-detail-image"
                  loading="lazy"
                />
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default PhotoDetailPage;
