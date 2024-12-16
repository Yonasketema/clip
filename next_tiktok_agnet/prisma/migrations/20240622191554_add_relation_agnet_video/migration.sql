/*
  Warnings:

  - A unique constraint covering the columns `[agentWorkId]` on the table `CreatedVideo` will be added. If there are existing duplicate values, this will fail.
  - Added the required column `agentWorkId` to the `CreatedVideo` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "CreatedVideo" ADD COLUMN     "agentWorkId" TEXT NOT NULL,
ADD COLUMN     "description" TEXT,
ALTER COLUMN "productName" DROP NOT NULL,
ALTER COLUMN "status" DROP NOT NULL,
ALTER COLUMN "status" SET DEFAULT false,
ALTER COLUMN "productWebsite" DROP NOT NULL,
ALTER COLUMN "videoUrl" DROP NOT NULL;

-- CreateIndex
CREATE UNIQUE INDEX "CreatedVideo_agentWorkId_key" ON "CreatedVideo"("agentWorkId");

-- AddForeignKey
ALTER TABLE "CreatedVideo" ADD CONSTRAINT "CreatedVideo_agentWorkId_fkey" FOREIGN KEY ("agentWorkId") REFERENCES "AgentWork"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
