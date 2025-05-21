import React, { useState, useEffect, useRef } from 'react';
import * as d3 from 'd3';
import { blogPostApi } from '../api/client';

const QueueVisualization = () => {
  const [blogPosts, setBlogPosts] = useState([]);
  const [queue, setQueue] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [newPost, setNewPost] = useState({
    title: '',
    body: ''
  });
  
  const svgRef = useRef();
  const width = 700;
  const height = 200;
  
  useEffect(() => {
    const fetchBlogPosts = async () => {
      try {
        setLoading(true);
        const response = await blogPostApi.getNumericPosts();
        setBlogPosts(response.data);
      } catch (err) {
        console.error('Error fetching blog posts:', err);
        setError('Failed to load blog posts. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchBlogPosts();
  }, []);
  
  const renderQueue = () => {
    if (!svgRef.current) return;
    
    // Clear previous visualization
    d3.select(svgRef.current).selectAll("*").remove();
    
    const svg = d3.select(svgRef.current)
      .attr("width", width)
      .attr("height", height);
    
    // Add a background rectangle
    svg.append("rect")
      .attr("width", width)
      .attr("height", height)
      .attr("fill", "#f8fafc")
      .attr("stroke", "#e2e8f0")
      .attr("stroke-width", 2);
    
    // Draw queue elements (from left to right)
    const elements = svg.selectAll(".queue-element")
      .data(queue)
      .enter()
      .append("g")
      .attr("class", "queue-element")
      .attr("transform", (d, i) => `translate(${50 + i * 110}, 50)`);
    
    // Draw rectangles for queue elements
    elements.append("rect")
      .attr("width", 100)
      .attr("height", 100)
      .attr("fill", (d, i) => {
        if (i === 0) return "#48bb78"; // Front (green)
        if (i === queue.length - 1) return "#4299e1"; // Rear (blue)
        return "#a0aec0"; // Middle (gray)
      })
      .attr("stroke", "#2d3748")
      .attr("stroke-width", 2);
    
    // Add IDs to queue elements
    elements.append("text")
      .attr("x", 50)
      .attr("y", 30)
      .attr("text-anchor", "middle")
      .attr("fill", "#fff")
      .attr("font-weight", "bold")
      .text(d => `ID: ${d.id}`);
    
    // Add titles to queue elements
    elements.append("text")
      .attr("x", 50)
      .attr("y", 50)
      .attr("text-anchor", "middle")
      .attr("fill", "#fff")
      .attr("font-size", "12px")
      .text(d => {
        const title = d.title;
        return title.length > 12 ? title.substring(0, 9) + '...' : title;
      });
    
    // Add tooltips with full post info
    elements.append("title")
      .text(d => `ID: ${d.id}\nTitle: ${d.title}\nBody: ${typeof d.body === 'number' ? `ASCII Sum: ${d.body}` : d.body}`);
    
    // Add "FRONT" and "REAR" labels if queue is not empty
    if (queue.length > 0) {
      // Front label
      svg.append("text")
        .attr("x", 100)
        .attr("y", 30)
        .attr("text-anchor", "middle")
        .attr("font-size", "14px")
        .attr("font-weight", "bold")
        .text("FRONT");
      
      // Rear label
      svg.append("text")
        .attr("x", 50 + (queue.length - 1) * 110 + 50)
        .attr("y", 30)
        .attr("text-anchor", "middle")
        .attr("font-size", "14px")
        .attr("font-weight", "bold")
        .text("REAR");
    }
  };
  
  useEffect(() => {
    renderQueue();
  }, [queue]);
  
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewPost(prev => ({
      ...prev,
      [name]: value
    }));
  };
  
  const handleEnqueue = (post) => {
    // Check queue size limit to avoid overflow in visualization
    if (queue.length >= 6) {
      alert('Queue is full! (Maximum 6 elements for visualization)');
      return;
    }
    
    setQueue(prev => [...prev, post]);
  };
  
  const handleDequeue = () => {
    if (queue.length === 0) {
      alert('Queue is empty!');
      return;
    }
    
    // Create a copy of the queue and remove the front element
    const [dequeuedElement, ...restQueue] = queue;
    
    setQueue(restQueue);
    
    return dequeuedElement;
  };
  
  const handleEnqueueCustom = (e) => {
    e.preventDefault();
    
    if (!newPost.title || !newPost.body) {
      alert('Both title and body are required');
      return;
    }
    
    // Create a mock blog post
    const mockPost = {
      id: queue.length > 0 ? Math.max(...queue.map(post => post.id)) + 1 : 1,
      title: newPost.title,
      body: newPost.body,
      user_id: 1 // Default user ID
    };
    
    handleEnqueue(mockPost);
    
    // Reset form
    setNewPost({
      title: '',
      body: ''
    });
  };
  
  if (loading && blogPosts.length === 0) {
    return (
      <div className="flex justify-center items-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-blue-500"></div>
      </div>
    );
  }
  
  if (error) {
    return (
      <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded">
        <p>{error}</p>
      </div>
    );
  }

  return (
    <div>
      <h1 className="text-2xl font-bold mb-6">Queue Visualization</h1>
      
      <div className="bg-white shadow-md rounded-lg p-6 mb-6">
        <h2 className="text-xl font-semibold mb-4">About Queues</h2>
        <p className="mb-4">
          A Queue is a linear data structure that follows the First In, First Out (FIFO) principle.
          The first element added to the queue is the first one to be removed.
        </p>
        <p>
          This visualization demonstrates queue operations like enqueue (add an element to the rear)
          and dequeue (remove an element from the front). The queue is used to store blog posts.
        </p>
      </div>
      
      <div className="bg-white shadow-md rounded-lg p-6 mb-6">
        <h2 className="text-xl font-semibold mb-4">Queue Visualization</h2>
        <div className="overflow-x-auto">
          <svg ref={svgRef}></svg>
        </div>
        {queue.length === 0 && (
          <p className="text-center mt-4 text-gray-500">
            Queue is empty. Enqueue some elements!
          </p>
        )}
      </div>
      
      <div className="bg-white shadow-md rounded-lg p-6">
        <h2 className="text-xl font-semibold mb-4">Queue Operations</h2>
        
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h3 className="font-medium mb-4">Enqueue a Blog Post</h3>
            <div className="overflow-auto max-h-60 mb-4">
              <table className="min-w-full divide-y divide-gray-200">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
                    <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Title</th>
                    <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Action</th>
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                  {blogPosts.length === 0 ? (
                    <tr>
                      <td colSpan="3" className="px-4 py-2 text-center text-sm text-gray-500">
                        No blog posts available
                      </td>
                    </tr>
                  ) : (
                    blogPosts.slice(0, 5).map((post) => (
                      <tr key={post.id} className="hover:bg-gray-50">
                        <td className="px-4 py-2 whitespace-nowrap text-sm font-medium text-gray-900">{post.id}</td>
                        <td className="px-4 py-2 whitespace-nowrap text-sm text-gray-500">{post.title}</td>
                        <td className="px-4 py-2 whitespace-nowrap text-sm font-medium">
                          <button
                            onClick={() => handleEnqueue(post)}
                            className="text-blue-600 hover:text-blue-900"
                          >
                            Enqueue
                          </button>
                        </td>
                      </tr>
                    ))
                  )}
                </tbody>
              </table>
            </div>
          </div>
          
          <div>
            <h3 className="font-medium mb-4">Enqueue a Custom Post</h3>
            <form onSubmit={handleEnqueueCustom} className="space-y-3">
              <div>
                <input
                  type="text"
                  name="title"
                  value={newPost.title}
                  onChange={handleInputChange}
                  className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  placeholder="Title"
                />
              </div>
              <div>
                <textarea
                  name="body"
                  value={newPost.body}
                  onChange={handleInputChange}
                  className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                  placeholder="Body"
                  rows="3"
                ></textarea>
              </div>
              <button
                type="submit"
                className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
              >
                Enqueue Custom Post
              </button>
            </form>
          </div>
        </div>
        
        <div className="mt-6 flex justify-between items-center">
          <button
            onClick={handleDequeue}
            className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded"
          >
            Dequeue
          </button>
          <div className="text-sm text-gray-600">
            Queue Size: {queue.length}
          </div>
        </div>
      </div>
    </div>
  );
};

export default QueueVisualization;
