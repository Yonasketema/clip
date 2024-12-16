import prisma from "@/lib/db";
import { NextResponse } from "next/server";

export async function POST() {
  const res = await prisma.agentWork.create({
    data: {
      events_message: [],
      status: "WORKING",
      output: "",
    },
  });
  return NextResponse.json(res);
}
