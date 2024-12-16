-- CreateTable
CREATE TABLE "CreatedVideo" (
    "id" TEXT NOT NULL,
    "updateAt" TIMESTAMP(3) NOT NULL,
    "createAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "productName" TEXT NOT NULL,
    "status" BOOLEAN NOT NULL,
    "productWebsite" TEXT NOT NULL,
    "videoUrl" TEXT NOT NULL,

    CONSTRAINT "CreatedVideo_pkey" PRIMARY KEY ("id")
);
