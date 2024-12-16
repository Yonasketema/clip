"use client";

import { createAgentWork, getAgentsData } from "@/lib/api";
import { useEffect, useRef, useState } from "react";
import { AiFillRobot } from "react-icons/ai";
import { BiLoader } from "react-icons/bi";
import { FaTiktok } from "react-icons/fa";
import FileContainer from "./FileContainer";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
} from "@/components/ui/card";

type PropsType = {
  model: boolean;
  productName?: string;
  description?: string;
  url?: string;
  video?: File;
  image?: File;
  interval?: number;
  numberOfVideos?: number;
  page: string;
};

export default function FeedbackUi({
  model,
  description,
  productName,
  url,
  image,
  video,
  interval,
  numberOfVideos,
  page,
}: PropsType) {
  const [result, setResult] = useState();
  const [error, setError] = useState();
  const [isLoading, setIsLoading] = useState(false);
  const [currentJobId, setCurrentJobId] = useState<string>("");
  const [events, setEvents] = useState<string[]>([""]);

  const outputContainerRef = useRef<HTMLInputElement | null>(null);

  const scrollToBottom = () => {
    if (outputContainerRef.current !== null) {
      outputContainerRef.current.scrollTo({
        top: outputContainerRef.current.scrollHeight,
        behavior: "smooth",
      });
    }
  };

  async function handleFetch() {
    setIsLoading(true);

    const formData = new FormData();
    formData.append("description", description || "");
    formData.append("url", url || "");
    formData.append("ProductName", productName || "");
    formData.append("image", image || "");
    formData.append("video", video || "");
    formData.append("interval", String(interval) || "");
    formData.append("videoNumber", String(numberOfVideos) || "");
    formData.append("page", page);

    try {
      const job = await createAgentWork();
      setCurrentJobId(job.id);

      const res = await fetch(
        new Request(`http://localhost:8000/create/${job.id}`),
        {
          method: "POST",
          body: formData,
        }
      );

      const data = await res.json();

      setResult(data.message);
    } catch (e) {
      setIsLoading(false);
      setError(e.message ? e.message : "error");
    }
  }

  useEffect(() => {
    let intervalId: number;

    const fetchJobStatus = async () => {
      try {
        const response = await getAgentsData(currentJobId);

        setEvents(response.events_message);
        setIsLoading(
          !(response.status === "END" || response.status === "ERROR")
        );

        if (response.status === "END" || response.status === "ERROR") {
          if (intervalId) {
            clearInterval(intervalId);
          }
        }
      } catch (error) {
        if (intervalId) {
          clearInterval(intervalId);
          setError(e.message ? e.message : "error");
        }

        console.error(error);
      }
    };

    if (currentJobId !== "") {
      intervalId = setInterval(fetchJobStatus, 3000) as unknown as number;
    }

    return () => {
      if (intervalId) {
        clearInterval(intervalId);
      }
    };
  }, [currentJobId]);

  // useEffect(() => {
  //   scrollToBottom();
  // }, [events]);

  useEffect(() => {
    if (model) {
      handleFetch();
    }
  }, []);

  return (
    <div className="p-5 px-9  h-full w-full">
      {!model && (
        <Button size="lg" onClick={handleFetch} disabled={isLoading}>
          Start Creating
          {isLoading && <BiLoader size={21} className="animate-spin ml-4" />}
        </Button>
      )}

      <div
        ref={outputContainerRef}
        className="flex flex-col gap-4  w-full h-96  px-7 mt-3 border border-slate-500 rounded-md overflow-y-auto"
      >
        <Card className="flex  gap-6 mt-3  bg-blue-100 rounded-lg border border-blue-300 p-5 text-gray-800 ">
          {/* <div className="w-[80%] h-[80%]">
            <AiFillRobot size={"7%"} className="text-slate-800" />
          </div> */}
          {!error && isLoading && (
            <p className="flex gap-7 text-green-500 font-semibold ">
              Creating ...{" "}
              {isLoading && model && (
                <BiLoader size={23} className="animate-spin ml-4" />
              )}
            </p>
          )}
          {error && <p className="text-red-600">{error}</p>}
        </Card>

        {isLoading && (
          <Card className="flex items-start gap-6 mt-3  bg-blue-100 rounded-lg border border-blue-300 p-5 text-gray-800 ">
            <p className="text-gray-900 font-medium">Starting Task ...</p>
          </Card>
        )}

        {events.map(
          (message, i) =>
            message && (
              <div
                key={i}
                className="flex items-start gap-6 mt-3  bg-blue-100 rounded-lg border border-blue-300 p-5 text-gray-800 "
              >
                <div className="w-7 h-7">
                  <AiFillRobot size={"100%"} className="text-blue-900" />
                </div>

                {/^(ftp|http|https):\/\/[^ "]+$/.test(message) ? (
                  <FileContainer url={message} />
                ) : (
                  <p className="text-gray-900 font-medium">{message}</p>
                )}
              </div>
            )
        )}
        <div>{result && result}</div>
      </div>
    </div>
  );
}
