import React from "react";
import "./Header.css";
import UploadForm from "../UploadForm/UploadForm";

const Header = () => {
  return (
    <div className="h-wrapper">
      <div className="h-left">
        <div className="logoImage">
          <img className="imagelogo" src="./logo.png" alt="" />
          <span className="planetText"> Planet</span>
        </div>
        <div className="textheader">
          <span className="primaryText">formely</span>
          <span className="secondaryText">DPhi</span>
        </div>
      </div>

      <div className="h-right">
        <UploadForm></UploadForm>
      </div>
    </div>
  );
};

export default Header;
