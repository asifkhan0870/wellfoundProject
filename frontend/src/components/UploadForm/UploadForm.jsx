import React, { useState } from "react";
import axios from "axios";
import { CiCirclePlus } from "react-icons/ci";
import "./UploadForm.css";

const UploadForm = () => {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append("file", file);

    const response = await axios.post(
      "http://localhost:8000/upload/",
      formData,
      {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      }
    );

    console.log(response.data);
  };

  return (
    <form className="uploadPdf" onSubmit={handleSubmit}>
      <button className="btn">
        <input type="file" onChange={handleFileChange} />
      </button>
    </form>
  );
};

export default UploadForm;
