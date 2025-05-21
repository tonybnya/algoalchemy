import React from 'react';

/**
 * Loading component with different size options
 */
const Loading = ({ size = 'medium', text = 'Loading...' }) => {
  const sizes = {
    small: 'h-6 w-6',
    medium: 'h-12 w-12',
    large: 'h-16 w-16'
  };
  
  const spinnerSize = sizes[size] || sizes.medium;
  
  return (
    <div className="flex flex-col items-center justify-center p-4">
      <div className={`animate-spin rounded-full ${spinnerSize} border-t-2 border-b-2 border-blue-500`}></div>
      {text && <p className="mt-2 text-gray-600">{text}</p>}
    </div>
  );
};

export default Loading;
