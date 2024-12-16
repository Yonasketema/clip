import Image from "next/image";
import React from "react";
import ReactAudioPlayer from "react-audio-player";

type FileContainerProps = {
  url: string;
};

function FileContainer({ url }: FileContainerProps) {
  const fileName = new URL(url).pathname.split("/").pop();
  const extension = fileName?.split(".").pop() as string;

  console.log("UUUU", url);

  return (
    <>
      {["jpg", "jpeg", "png", "gif"].includes(extension) && (
        <img
          // layout="responsive"
          src={`${url}`}
          alt={url}
          width={1080}
          height={1920}
        />
      )}
      {["mp3", "wav"].includes(extension) && (
        <ReactAudioPlayer src={`${url}`} controls />
      )}
      {["mp4", "avi", "mov"].includes(extension) && (
        <video controls width={400}>
          <source src={`${url}`} type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      )}
    </>
  );
}

export default FileContainer;
