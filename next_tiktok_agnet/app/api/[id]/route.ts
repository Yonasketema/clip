import prisma from "@/lib/db";
import { NextResponse } from "next/server";

export async function POST(
  req: Request,
  { params }: { params: { id: string } }
) {
  const data = await req.json();

  await prisma.agentWork.update({
    where: {
      id: params.id,
    },
    data: {
      events_message: {
        push: data.event_message.replace(/\n/g, " "),
      },
      status: data.status,
      output: data.output,
    },
  });

  return NextResponse.json({});
}
export async function GET(
  req: Request,
  { params }: { params: { id: string } }
) {
  const data = await prisma.agentWork.findFirst({
    where: {
      id: params.id,
    },
  });

  return NextResponse.json({
    data: data,
  });
}
