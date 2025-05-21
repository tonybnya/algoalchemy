import React, { useState, useEffect, useRef } from 'react';
import * as d3 from 'd3';
import { blogPostApi } from '../api/client';

const StackVisualization = () => {
  const [blogPosts, setBlogPosts] = useState([]);
  const [stack, setStack] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [newPost, setNewPost] = useState({
    title: '',
    body: ''
  });
  
  const svgRef = useRef();
  const width = 300;
  const height = 500;
  
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
  
  const renderStack = () => {
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
    
    // Draw stack elements (from bottom to top)
    const elements = svg.selectAll(".stack-element")
      .data(stack)
      .enter()
      .append("g")
      .attr("class", "stack-element")
      .attr("transform", (d, i) => `translate(0, ${height - 60 * (i + 1)})`);
    
    // Draw rectangles for stack elements
    elements.append("rect")
      .attr("width", width)
      .attr("height", 50)
      .attr("fill", (d, i) => i === stack.length - 1 ? "#4299e1" : "#90cdf4")
      .attr("stroke", "#2b6cb0")
      .attr("stroke-width", 2);
    
    // Add IDs to stack elements
    elements.append("text")
      .attr("x", 20)
      .attr("y", 20)
      .attr("fill", "#fff")
      .attr("font-weight", "bold")
      .text(d => `ID: ${d.id}`);
    
    // Add titles to stack elements
    elements.append("text")
      .attr("x", 20)
      .attr("y", 35)
      .attr("fill", "#fff")
      .text(d => {
        const title = d.title;
        return title.length > 25 ? title.substring(0, 22) + '...' : title;
      });
    
    // Add tooltips with full post info
    elements.append("title")
      .text(d => `ID: ${d.id}\nTitle: ${d.title}\nBody: ${typeof d.body === 'number' ? `ASCII Sum: ${d.body}` : d.body}`);
    
    // Add "TOP" label if stack is not empty
    if (stack.length > 0) {
      svg.append("text")
        .attr("x", width / 2)
        .attr("y", height - 60 * stack.length - 10)
        .attr("text-anchor", "middle")
        .attr("font-size", "14px")
        .attr("font-weight", "bold")
        .text("TOP");
    }
  };
  
  useEffect(() => {
    renderStack();
  }, [stack]);
  
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewPost(prev => ({
      ...prev,
      [name]: value
    }));
  };
  
  const handlePush = (post) => {
    // Check stack size limit to avoid overflow in visualization
    if (stack.length >= 8) {
      alert('Stack is full! (Maximum 8 elements for visualization)');
      return;
    }
    
    setStack(prev => [...prev, post]);
  };
  
  const handlePop = () => {
    if (stack.length === 0) {
      alert('Stack is empty!');
      return;
    }
    
    // Create a copy of the stack and remove the top element
    const newStack = [...stack];
    const poppedElement = newStack.pop();
    
    setStack(newStack);
    
    return poppedElement;
  };
  
  const handlePushCustom = (e) => {
    e.preventDefault();
    
    if (!newPost.title || !newPost.body) {
      alert('Both title and body are required');
      return;
    }
    
    // Create a mock blog post
    const mockPost = {
      id: stack.length > 0 ? Math.max(...stack.map(post => post.id)) + 1 : 1,
      title: newPost.title,
      body: newPost.body,
      user_id: 1 // Default user ID
    };
    
    handlePush(mockPost);
    
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
      <h1 className="text-2xl font-bold mb-6">Stack Visualization</h1>
      
      <div className="bg-white shadow-md rounded-lg p-6 mb-6">
        <h2 className="text-xl font-semibold mb-4">About Stacks</h2>
        <p className="mb-4">
          A Stack is a linear data structure that follows the Last In, First Out (LIFO) principle.
          The last element added to the stack is the first one to be removed.
        </p>
        <p>
          This visualization demonstrates stack operations like push (add an element to the top)
          and pop (remove the top element). The stack is used to store blog posts.
        </p>
      </div>
      
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white shadow-md rounded-lg p-6">
          <h2 className="text-xl font-semibold mb-4">Stack Operations</h2>
          
          <div className="mb-6">
            <h3 className="font-medium mb-2">Push a Blog Post</h3>
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
                    blogPosts.map((post) => (
                      <tr key={post.id} className="hover:bg-gray-50">
                        <td className="px-4 py-2 whitespace-nowrap text-sm font-medium text-gray-900">{post.id}</td>
                        <td className="px-4 py-2 whitespace-nowrap text-sm text-gray-500">{post.title}</td>
                        <td className="px-4 py-2 whitespace-nowrap text-sm font-medium">
                          <button
                            onClick={() => handlePush(post)}
                            className="text-blue-600 hover:text-blue-900"
                          >
                            Push
                          </button>
                        </td>
                      </tr>
                    ))
                  )}
                </tbody>
              </table>
            </div>
            
            <h3 className="font-medium mb-2">Push a Custom Post</h3>
            <form onSubmit={handlePushCustom} className="space-y-3">
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
                Push Custom Post
              </button>
            </form>
          </div>
          
          <div className="flex justify-between items-center">
            <button
              onClick={handlePop}
              className="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded"
            >
              Pop
            </button>
            <div className="text-sm text-gray-600">
              Stack Size: {stack.length}
            </div>
          </div>
        </div>
        
        <div className="bg-white shadow-md rounded-lg p-6">
          <h2 className="text-xl font-semibold mb-4">Stack Visualization</h2>
          <div className="flex justify-center">
            <svg ref={svgRef}></svg>
          </div>
          {stack.length === 0 && (
            <p className="text-center mt-4 text-gray-500">
              Stack is empty. Push some elements!
            </p>
          )}
        </div>
      </div>
    </div>
  );
};

export default StackVisualization;
