import prisma from "@/lib/db";
import { revalidatePath } from "next/cache";
import { NextResponse } from "next/server";

export async function POST(
  req: Request,
  { params }: { params: { agentId: string } }
) {
  const data = await req.json();

  const newCreatedVideo = await prisma.createdVideo.create({
    data: {
      agentWorkId: params.agentId,
      videoUrl: data.videoUrl,
      productName: data.productName || "",
      description: data.description || "",
      productWebsite: data.productWebsite || "",
      page: data.page || "",
    },
  });

  revalidatePath("/affiliate");

  return NextResponse.json(newCreatedVideo);
}
