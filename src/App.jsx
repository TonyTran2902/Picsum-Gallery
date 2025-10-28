import { Navigate, Route, Routes } from 'react-router-dom';
import PhotosPage from './pages/PhotosPage';
import PhotoDetailPage from './pages/PhotoDetailPage';

const App = () => (
  <div className="app-shell">
    <Routes>
      <Route path="/" element={<Navigate to="/photos" replace />} />
      <Route path="/photos" element={<PhotosPage />} />
      <Route path="/photos/:id" element={<PhotoDetailPage />} />
      <Route path="*" element={<Navigate to="/photos" replace />} />
    </Routes>
  </div>
);

export default App;
