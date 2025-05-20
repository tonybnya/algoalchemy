import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout';

// Lazy load pages for better performance
const Dashboard = React.lazy(() => import('./pages/Dashboard'));
const Users = React.lazy(() => import('./pages/Users'));
const UserForm = React.lazy(() => import('./pages/UserForm'));
const BlogPosts = React.lazy(() => import('./pages/BlogPosts'));
const BlogPostForm = React.lazy(() => import('./pages/BlogPostForm'));
const BSTVisualization = React.lazy(() => import('./visualizations/BSTVisualization'));
const LinkedListVisualization = React.lazy(() => import('./visualizations/LinkedListVisualization'));
const StackVisualization = React.lazy(() => import('./visualizations/StackVisualization'));
const QueueVisualization = React.lazy(() => import('./visualizations/QueueVisualization'));
const HashMapVisualization = React.lazy(() => import('./visualizations/HashMapVisualization'));
import Loading from './components/Loading';

function App() {
  return (
    <BrowserRouter>
      <React.Suspense fallback={<Loading size="large" text="Loading page..." />}>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Dashboard />} />
            
            {/* User Routes */}
            <Route path="users" element={<Users />} />
            <Route path="users/new" element={<UserForm />} />
            <Route path="users/edit/:id" element={<UserForm />} />
            
            {/* Blog Post Routes */}
            <Route path="blogposts" element={<BlogPosts />} />
            <Route path="blogposts/new/:userId" element={<BlogPostForm />} />
            
            {/* Data Structure Visualization Routes */}
            <Route path="visualize/bst" element={<BSTVisualization />} />
            <Route path="visualize/linkedlist" element={<LinkedListVisualization />} />
            <Route path="visualize/stack" element={<StackVisualization />} />
            <Route path="visualize/queue" element={<QueueVisualization />} />
            <Route path="visualize/hashmap" element={<HashMapVisualization />} />
            
            {/* Fallback route */}
            <Route path="*" element={<Navigate to="/" replace />} />
          </Route>
        </Routes>
      </React.Suspense>
    </BrowserRouter>
  );
}

export default App;
