"use client";

import { createAgentWork, getAgentsData } from "@/lib/api";
import { useEffect, useRef, useState } from "react";
import { AiFillRobot } from "react-icons/ai";
import { BiLoader } from "react-icons/bi";
import { FaTiktok } from "react-icons/fa";
import FileContainer from "../components/FileContainer";
import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
} from "@/components/ui/card";
import ChooseModeModal from "@/components/ChooseModeModal";
import FeedbackUi from "@/components/FeedbackUi";

export default function Home() {
  return (
    <main className="p-5 px-9">
      <header className="py-3 flex justify-end gap-3 items-center">
        <FaTiktok size={21} />
        <h1 className="font-bold font-sans text-lg">TrendSpot </h1>
      </header>

      <FeedbackUi model={false} />

      <ChooseModeModal />
    </main>
  );
}
