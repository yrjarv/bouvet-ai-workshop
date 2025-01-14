import React from "react";
import "../styles/App.css";

const UploadIcon: React.FC = () => {
  return (
    <svg
      width="110"
      height="110"
      viewBox="0 0 50 50"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <path
        d="M37.25 27.75V34.0833C37.25 34.9232 36.9164 35.7286 36.3225 36.3225C35.7286 36.9164 34.9232 37.25 34.0833 37.25H11.9167C11.0768 37.25 10.2714 36.9164 9.6775 36.3225C9.08363 35.7286 8.75 34.9232 8.75 34.0833V27.75"
        stroke="#11133C"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
      <path
        d="M30.9167 16.6667L23 8.75L15.0833 16.6667"
        stroke="#11133C"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
      <path
        d="M23 8.75V27.75"
        stroke="#11133C"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
};

export default UploadIcon;
