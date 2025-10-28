import PropTypes from 'prop-types';
import { Link } from 'react-router-dom';

const PhotoCard = ({ photo }) => {
  const { id, author } = photo;
  const thumbnailUrl = `https://picsum.photos/id/${id}/400/300`;

  return (
    <Link to={`/photos/${id}`} className="card h-100 shadow-sm">
      <img
        src={thumbnailUrl}
        alt={`Thumbnail for photo ${id} by ${author}`}
        className="card-img-top thumbnail-image"
        loading="lazy"
        width="400"
        height="300"
      />
      <div className="card-body">
        <h2 className="h6 card-title mb-1 text-truncate">{author || 'Unknown Author'}</h2>
        <p className="card-text text-muted small mb-0">Tap to view details</p>
      </div>
    </Link>
  );
};

PhotoCard.propTypes = {
  photo: PropTypes.shape({
    id: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
    author: PropTypes.string,
  }).isRequired,
};

export default PhotoCard;
