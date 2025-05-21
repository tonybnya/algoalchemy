import React, { useState, useEffect, useRef } from 'react';
import * as d3 from 'd3';

const HashMapVisualization = () => {
  const [hashMap, setHashMap] = useState(new Map());
  const [buckets, setBuckets] = useState([]);
  const [key, setKey] = useState('');
  const [value, setValue] = useState('');
  const [searchKey, setSearchKey] = useState('');
  const [searchResult, setSearchResult] = useState(null);
  const [bucketSize, setBucketSize] = useState(10);
  
  const svgRef = useRef();
  const width = 700;
  const height = 500;
  
  // Simple hash function for demonstration
  const hashFunction = (key) => {
    let hash = 0;
    for (let i = 0; i < key.length; i++) {
      hash = (hash + key.charCodeAt(i)) % bucketSize;
    }
    return hash;
  };
  
  const initializeBuckets = (size) => {
    const newBuckets = Array(size).fill().map(() => []);
    
    // Transfer existing values to new buckets if hashMap has entries
    if (hashMap.size > 0) {
      const newHashMap = new Map();
      
      for (const [k, v] of hashMap.entries()) {
        const hash = hashFunction(k);
        newBuckets[hash].push({ key: k, value: v });
        newHashMap.set(k, v);
      }
      
      setHashMap(newHashMap);
    }
    
    setBuckets(newBuckets);
  };
  
  useEffect(() => {
    initializeBuckets(bucketSize);
  }, [bucketSize]);
  
  const renderHashMap = () => {
    if (!svgRef.current) return;
    
    // Clear previous visualization
    d3.select(svgRef.current).selectAll("*").remove();
    
    const svg = d3.select(svgRef.current)
      .attr("width", width)
      .attr("height", height);
    
    const bucketHeight = 40;
    const bucketWidth = width - 100;
    const startX = 50;
    const startY = 50;
    
    // Draw the buckets
    svg.selectAll(".bucket-rect")
      .data(buckets)
      .enter()
      .append("rect")
      .attr("class", "bucket-rect")
      .attr("x", startX)
      .attr("y", (d, i) => startY + i * bucketHeight)
      .attr("width", bucketWidth)
      .attr("height", bucketHeight - 5)
      .attr("fill", "#f7fafc")
      .attr("stroke", "#cbd5e0")
      .attr("stroke-width", 1);
    
    // Draw bucket indices
    svg.selectAll(".bucket-index")
      .data(buckets)
      .enter()
      .append("text")
      .attr("class", "bucket-index")
      .attr("x", startX - 10)
      .attr("y", (d, i) => startY + i * bucketHeight + bucketHeight / 2)
      .attr("text-anchor", "end")
      .attr("dominant-baseline", "middle")
      .attr("font-size", "12px")
      .text((d, i) => i);
    
    // Draw bucket entries
    buckets.forEach((bucket, bucketIndex) => {
      const entries = svg.selectAll(`.bucket-entry-${bucketIndex}`)
        .data(bucket)
        .enter()
        .append("g")
        .attr("class", `bucket-entry-${bucketIndex}`)
        .attr("transform", (d, i) => {
          const x = startX + 10 + i * 120;
          const y = startY + bucketIndex * bucketHeight + bucketHeight / 2;
          return `translate(${x}, ${y})`;
        });
      
      // Entry background
      entries.append("rect")
        .attr("width", 110)
        .attr("height", 30)
        .attr("x", -55)
        .attr("y", -15)
        .attr("fill", (d) => {
          if (searchResult && d.key === searchResult.key) {
            return "#4299e1"; // Highlight found entry
          }
          return "#edf2f7";
        })
        .attr("stroke", "#a0aec0")
        .attr("stroke-width", 1)
        .attr("rx", 4);
      
      // Entry key
      entries.append("text")
        .attr("text-anchor", "middle")
        .attr("dominant-baseline", "middle")
        .attr("font-size", "12px")
        .attr("font-weight", "bold")
        .attr("fill", (d) => searchResult && d.key === searchResult.key ? "#fff" : "#4a5568")
        .text(d => {
          const displayKey = d.key.length > 10 ? d.key.substring(0, 7) + '...' : d.key;
          return `${displayKey}: ${d.value}`;
        });
      
      // Add tooltips
      entries.append("title")
        .text(d => `Key: ${d.key}\nValue: ${d.value}`);
    });
  };
  
  useEffect(() => {
    renderHashMap();
  }, [buckets, searchResult]);
  
  const handleAddKeyValue = (e) => {
    e.preventDefault();
    
    if (!key || !value) {
      alert('Both key and value are required');
      return;
    }
    
    // Calculate hash
    const hash = hashFunction(key);
    
    // Store in HashMap
    setHashMap(prev => new Map(prev.set(key, value)));
    
    // Update buckets
    const newBuckets = [...buckets];
    
    // Check if key already exists in the bucket
    const existingIndex = newBuckets[hash].findIndex(entry => entry.key === key);
    
    if (existingIndex !== -1) {
      // Update existing entry
      newBuckets[hash][existingIndex].value = value;
    } else {
      // Add new entry
      newBuckets[hash].push({ key, value });
    }
    
    setBuckets(newBuckets);
    
    // Reset form
    setKey('');
    setValue('');
  };
  
  const handleSearch = (e) => {
    e.preventDefault();
    
    if (!searchKey) {
      alert('Please enter a key to search');
      return;
    }
    
    // Get the hash
    const hash = hashFunction(searchKey);
    
    // Find in the bucket
    const entry = buckets[hash].find(entry => entry.key === searchKey);
    
    if (entry) {
      setSearchResult(entry);
    } else {
      setSearchResult(null);
      alert(`Key "${searchKey}" not found in the HashMap`);
    }
  };
  
  const handleResizeBuckets = (e) => {
    const newSize = parseInt(e.target.value);
    setBucketSize(newSize);
  };

  return (
    <div>
      <h1 className="text-2xl font-bold mb-6">HashMap Visualization</h1>
      
      <div className="bg-white shadow-md rounded-lg p-6 mb-6">
        <h2 className="text-xl font-semibold mb-4">About HashMaps</h2>
        <p className="mb-4">
          A HashMap is a data structure that stores key-value pairs. It uses a hash function
          to compute an index into an array of buckets or slots, from which the desired value can be found.
        </p>
        <p>
          This visualization demonstrates the internal workings of a HashMap with
          operations like adding key-value pairs and searching for values by key.
        </p>
      </div>
      
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
        <div className="bg-white shadow-md rounded-lg p-6">
          <h2 className="text-xl font-semibold mb-4">Add Key-Value Pair</h2>
          <form onSubmit={handleAddKeyValue} className="space-y-4">
            <div>
              <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="key">
                Key
              </label>
              <input
                type="text"
                id="key"
                value={key}
                onChange={(e) => setKey(e.target.value)}
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                placeholder="Enter key"
                required
              />
              {key && (
                <div className="mt-1 text-sm text-gray-500">
                  Hash: {hashFunction(key)}
                </div>
              )}
            </div>
            <div>
              <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="value">
                Value
              </label>
              <input
                type="text"
                id="value"
                value={value}
                onChange={(e) => setValue(e.target.value)}
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                placeholder="Enter value"
                required
              />
            </div>
            <button
              type="submit"
              className="w-full bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            >
              Add / Update
            </button>
          </form>
        </div>
        
        <div className="bg-white shadow-md rounded-lg p-6">
          <h2 className="text-xl font-semibold mb-4">Search by Key</h2>
          <form onSubmit={handleSearch} className="space-y-4">
            <div>
              <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="searchKey">
                Key
              </label>
              <input
                type="text"
                id="searchKey"
                value={searchKey}
                onChange={(e) => setSearchKey(e.target.value)}
                className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                placeholder="Enter key to search"
                required
              />
              {searchKey && (
                <div className="mt-1 text-sm text-gray-500">
                  Hash: {hashFunction(searchKey)}
                </div>
              )}
            </div>
            <button
              type="submit"
              className="w-full bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
            >
              Search
            </button>
          </form>
          
          {searchResult && (
            <div className="mt-4 p-4 bg-blue-100 rounded-md">
              <h3 className="font-semibold mb-2">Result:</h3>
              <p><span className="font-medium">Key:</span> {searchResult.key}</p>
              <p><span className="font-medium">Value:</span> {searchResult.value}</p>
              <p><span className="font-medium">Bucket Index:</span> {hashFunction(searchResult.key)}</p>
            </div>
          )}
        </div>
        
        <div className="bg-white shadow-md rounded-lg p-6">
          <h2 className="text-xl font-semibold mb-4">HashMap Settings</h2>
          <div className="space-y-4">
            <div>
              <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="bucketSize">
                Number of Buckets
              </label>
              <input
                type="range"
                id="bucketSize"
                min="5"
                max="15"
                value={bucketSize}
                onChange={handleResizeBuckets}
                className="w-full"
              />
              <div className="mt-1 text-sm text-gray-500 text-center">
                {bucketSize} buckets
              </div>
            </div>
            <div className="p-4 bg-gray-100 rounded-md">
              <h3 className="font-semibold mb-2">HashMap Stats:</h3>
              <p><span className="font-medium">Total Key-Value Pairs:</span> {hashMap.size}</p>
              <p><span className="font-medium">Hash Function:</span> sum of char codes % bucket size</p>
              <p><span className="font-medium">Collision Strategy:</span> Chaining (linked list)</p>
            </div>
          </div>
        </div>
      </div>
      
      <div className="bg-white shadow-md rounded-lg p-6 overflow-auto">
        <h2 className="text-xl font-semibold mb-4">HashMap Visualization</h2>
        <svg ref={svgRef}></svg>
      </div>
    </div>
  );
};

export default HashMapVisualization;
