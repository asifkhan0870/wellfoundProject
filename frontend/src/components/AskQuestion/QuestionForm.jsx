import React, { useState } from "react";
import { IoMdSend } from "react-icons/io";
import axios from "axios";
import "./QuestionForm.css";

const QuestionForm = () => {
  const [pdfId, setPdfId] = useState("");
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    const response = await axios.post("http://localhost:8000/ask/", {
      pdf_id: pdfId,
      question,
    });

    setAnswer(response.data.answer);
  };

  return (
    <div className="questionbox">
      <form className="questionform" onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="PDF ID"
          value={pdfId}
          onChange={(e) => setPdfId(e.target.value)}
        />
        <input
          type="text"
          placeholder="Your Question"
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
        />

        <button className="btnn" type="submit">
          Ask Question
        </button>
      </form>
      {answer && (
        <div>
          <h3>Answer:</h3>
          <p>{answer}</p>
        </div>
      )}
    </div>
  );
};

export default QuestionForm;
