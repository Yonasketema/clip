-- CreateEnum
CREATE TYPE "STATUS" AS ENUM ('STARTED', 'END');

-- CreateTable
CREATE TABLE "AgentWork" (
    "id" TEXT NOT NULL,
    "updateAt" TIMESTAMP(3) NOT NULL,
    "createAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "events_message" TEXT[],
    "status" "STATUS" NOT NULL,
    "output" TEXT NOT NULL,

    CONSTRAINT "AgentWork_pkey" PRIMARY KEY ("id")
);
