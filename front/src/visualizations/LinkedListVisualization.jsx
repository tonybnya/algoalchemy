import React, { useState, useEffect, useRef } from 'react';
import * as d3 from 'd3';
import { userApi } from '../api/client';

const LinkedListVisualization = () => {
  const [users, setUsers] = useState([]);
  const [linkedList, setLinkedList] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [viewMode, setViewMode] = useState('asc'); // 'asc' or 'desc'
  const [newUser, setNewUser] = useState({
    username: '',
    email: '',
    address: '',
    phone: ''
  });
  
  const svgRef = useRef();
  const width = 800;
  const height = 300;
  
  const fetchUsers = async (mode) => {
    try {
      setLoading(true);
      const response = mode === 'asc' 
        ? await userApi.getUsersAscending()
        : await userApi.getUsersDescending();
      
      setUsers(response.data);
      
      // Convert data to linked list format for visualization
      const nodes = response.data.map((user, index) => ({
        ...user,
        index: index,
        x: 100 + index * 150,
        y: height / 2
      }));
      
      setLinkedList(nodes);
    } catch (err) {
      console.error('Error fetching users:', err);
      setError('Failed to load users. Please try again later.');
    } finally {
      setLoading(false);
    }
  };
  
  useEffect(() => {
    fetchUsers(viewMode);
  }, [viewMode]);
  
  const renderLinkedList = () => {
    if (!svgRef.current || linkedList.length === 0) return;
    
    // Clear previous visualization
    d3.select(svgRef.current).selectAll("*").remove();
    
    const svg = d3.select(svgRef.current)
      .attr("width", width)
      .attr("height", height);
    
    // Draw arrows between nodes
    svg.selectAll(".link")
      .data(linkedList.slice(0, -1))
      .enter()
      .append("line")
      .attr("class", "link")
      .attr("x1", d => d.x + 50)
      .attr("y1", d => d.y)
      .attr("x2", (d, i) => linkedList[i + 1].x - 50)
      .attr("y2", (d, i) => linkedList[i + 1].y)
      .attr("stroke", "#999")
      .attr("stroke-width", 2)
      .attr("marker-end", "url(#arrow)");
    
    // Add arrow marker
    svg.append("defs").append("marker")
      .attr("id", "arrow")
      .attr("viewBox", "0 -5 10 10")
      .attr("refX", 8)
      .attr("refY", 0)
      .attr("markerWidth", 6)
      .attr("markerHeight", 6)
      .attr("orient", "auto")
      .append("path")
      .attr("d", "M0,-5L10,0L0,5")
      .attr("fill", "#999");
    
    // Create node groups
    const nodes = svg.selectAll(".node")
      .data(linkedList)
      .enter()
      .append("g")
      .attr("class", "node")
      .attr("transform", d => `translate(${d.x}, ${d.y})`);
    
    // Draw rectangles for nodes
    nodes.append("rect")
      .attr("width", 100)
      .attr("height", 60)
      .attr("x", -50)
      .attr("y", -30)
      .attr("rx", 5)
      .attr("fill", "#3182CE")
      .attr("stroke", "#2C5282")
      .attr("stroke-width", 2);
    
    // Add text (usernames) to nodes
    nodes.append("text")
      .attr("text-anchor", "middle")
      .attr("dy", 0)
      .attr("fill", "#fff")
      .text(d => d.username);
    
    // Add IDs under usernames
    nodes.append("text")
      .attr("text-anchor", "middle")
      .attr("dy", 20)
      .attr("fill", "#fff")
      .text(d => `ID: ${d.id}`);
    
    // Add tooltips with full user info
    nodes.append("title")
      .text(d => `ID: ${d.id}\nUsername: ${d.username}\nEmail: ${d.email}\nAddress: ${d.address}\nPhone: ${d.phone}`);
    
    // Add labels for head and tail
    if (linkedList.length > 0) {
      // Head label
      svg.append("text")
        .attr("x", linkedList[0].x)
        .attr("y", linkedList[0].y - 50)
        .attr("text-anchor", "middle")
        .attr("font-size", "14px")
        .attr("font-weight", "bold")
        .text("Head");
      
      // Tail label
      svg.append("text")
        .attr("x", linkedList[linkedList.length - 1].x)
        .attr("y", linkedList[linkedList.length - 1].y - 50)
        .attr("text-anchor", "middle")
        .attr("font-size", "14px")
        .attr("font-weight", "bold")
        .text("Tail");
    }
  };
  
  useEffect(() => {
    renderLinkedList();
  }, [linkedList]);
  
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setNewUser(prev => ({
      ...prev,
      [name]: value
    }));
  };
  
  const handleAddToHead = async (e) => {
    e.preventDefault();
    
    if (!newUser.username || !newUser.email || !newUser.address || !newUser.phone) {
      alert('All fields are required');
      return;
    }
    
    try {
      // Simulate adding to head for visualization purposes
      // In a real app, this would create a new user via API
      const mockUser = {
        id: Math.max(0, ...linkedList.map(user => user.id)) + 1,
        ...newUser
      };
      
      // Insert at the beginning of the array (for visualization only)
      const newList = [
        {
          ...mockUser,
          index: 0,
          x: 100,
          y: height / 2
        },
        ...linkedList.map((user, idx) => ({
          ...user,
          index: idx + 1,
          x: 100 + (idx + 1) * 150,
          y: height / 2
        }))
      ];
      
      setLinkedList(newList);
      
      // Reset form
      setNewUser({
        username: '',
        email: '',
        address: '',
        phone: ''
      });
    } catch (err) {
      console.error('Error adding user:', err);
    }
  };
  
  const handleAddToTail = async (e) => {
    e.preventDefault();
    
    if (!newUser.username || !newUser.email || !newUser.address || !newUser.phone) {
      alert('All fields are required');
      return;
    }
    
    try {
      // Simulate adding to tail for visualization purposes
      const mockUser = {
        id: Math.max(0, ...linkedList.map(user => user.id)) + 1,
        ...newUser
      };
      
      // Add to the end of the array
      const newList = [
        ...linkedList,
        {
          ...mockUser,
          index: linkedList.length,
          x: 100 + linkedList.length * 150,
          y: height / 2
        }
      ];
      
      setLinkedList(newList);
      
      // Reset form
      setNewUser({
        username: '',
        email: '',
        address: '',
        phone: ''
      });
    } catch (err) {
      console.error('Error adding user:', err);
    }
  };
  
  if (loading && users.length === 0) {
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
      <h1 className="text-2xl font-bold mb-6">Linked List Visualization</h1>
      
      <div className="bg-white shadow-md rounded-lg p-6 mb-6">
        <h2 className="text-xl font-semibold mb-4">About Linked Lists</h2>
        <p className="mb-4">
          A Linked List is a linear data structure where each element (node) contains 
          a reference to the next node in the sequence. The first node is called the "head",
          and the last node is called the "tail".
        </p>
        <p>
          This visualization shows users stored in a linked list structure, with operations
          to add nodes to the head or tail of the list, and view the list in ascending or descending order.
        </p>
      </div>
      
      <div className="bg-white shadow-md rounded-lg p-6 mb-6">
        <div className="flex justify-between items-center mb-4">
          <h2 className="text-xl font-semibold">List Operations</h2>
          <div className="flex space-x-2">
            <button
              onClick={() => setViewMode('asc')}
              className={`px-4 py-2 rounded ${
                viewMode === 'asc' 
                  ? 'bg-blue-500 text-white' 
                  : 'bg-gray-200 text-gray-800'
              }`}
            >
              Ascending Order
            </button>
            <button
              onClick={() => setViewMode('desc')}
              className={`px-4 py-2 rounded ${
                viewMode === 'desc' 
                  ? 'bg-blue-500 text-white' 
                  : 'bg-gray-200 text-gray-800'
              }`}
            >
              Descending Order
            </button>
          </div>
        </div>
        
        <form className="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-4 mb-4">
          <div>
            <label className="block text-gray-700 text-sm font-bold mb-2">Username</label>
            <input
              type="text"
              name="username"
              value={newUser.username}
              onChange={handleInputChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="Username"
            />
          </div>
          <div>
            <label className="block text-gray-700 text-sm font-bold mb-2">Email</label>
            <input
              type="email"
              name="email"
              value={newUser.email}
              onChange={handleInputChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="Email"
            />
          </div>
          <div>
            <label className="block text-gray-700 text-sm font-bold mb-2">Address</label>
            <input
              type="text"
              name="address"
              value={newUser.address}
              onChange={handleInputChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="Address"
            />
          </div>
          <div>
            <label className="block text-gray-700 text-sm font-bold mb-2">Phone</label>
            <input
              type="text"
              name="phone"
              value={newUser.phone}
              onChange={handleInputChange}
              className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
              placeholder="Phone"
            />
          </div>
        </form>
        
        <div className="flex space-x-2">
          <button
            onClick={handleAddToHead}
            className="bg-green-500 hover:bg-green-600 text-white py-2 px-4 rounded"
          >
            Add to Head
          </button>
          <button
            onClick={handleAddToTail}
            className="bg-indigo-500 hover:bg-indigo-600 text-white py-2 px-4 rounded"
          >
            Add to Tail
          </button>
        </div>
      </div>
      
      <div className="bg-white shadow-md rounded-lg p-6 overflow-auto">
        <h2 className="text-xl font-semibold mb-4">Linked List Visualization</h2>
        <p className="mb-4 text-sm text-gray-600">
          Showing users in {viewMode === 'asc' ? 'ascending' : 'descending'} order. 
          Hover over nodes to see user details.
        </p>
        {linkedList.length > 0 ? (
          <div className="flex justify-center">
            <svg ref={svgRef}></svg>
          </div>
        ) : (
          <p className="text-center text-gray-500">No data available for visualization.</p>
        )}
      </div>
    </div>
  );
};

export default LinkedListVisualization;
