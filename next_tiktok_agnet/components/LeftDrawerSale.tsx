"use client";

import React, { useState } from "react";

import { PlusCircle } from "lucide-react";

import { Input } from "@/components/ui/input";

import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog";

import { Button } from "@/components/ui/button";
import { Label } from "@/components/ui/label";
import { Textarea } from "@/components/ui/textarea";
import FeedbackUi from "./FeedbackUi";

import {
  Sheet,
  SheetClose,
  SheetContent,
  SheetDescription,
  SheetFooter,
  SheetHeader,
  SheetTitle,
  SheetTrigger,
} from "@/components/ui/sheet";

import Image from "next/image";
import { Upload } from "lucide-react";

import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";

function LeftDrawerSale() {
  const [description, setDescription] = useState(
    "Become the Person You Dream to Be."
  );
  const [productName, setProductName] = useState("wehusstle");
  const [url, setUrl] = useState("https://wehusstle.vercel.app/");
  const [numberOfVideos, setNumberOfVideos] = useState<number>(1);
  const [interval, setInterval] = useState<number>(0);
  const [videoURL, setVideoURL] = useState<File>();
  const [imageURL, setImageURL] = useState<File>();

  const [open, setOpen] = React.useState(false);

  function handleCreateVideos() {
    console.log(`${description} ${productName} ${url} `);
    console.log(imageURL);
    setOpen(true);
  }

  const handleVideoUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      setVideoURL(file);
    }
  };
  const handleImageUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];
    if (file) {
      setImageURL(file);
    }
  };

  return (
    <span className="sr-only sm:not-sr-only sm:whitespace-nowrap">
      <Sheet>
        <SheetTrigger asChild>
          <Button>
            <PlusCircle className="h-3.5 w-3.5" /> Add Product
          </Button>
        </SheetTrigger>
        <SheetContent>
          <SheetHeader>
            <SheetTitle>Add new product</SheetTitle>
            <SheetDescription>new product</SheetDescription>
          </SheetHeader>
          <div className="grid gap-4 py-4">
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="name" className="text-right">
                ProductName
              </Label>
              <Input
                id="name"
                value={productName}
                onChange={(e) => setProductName(e.target.value)}
                className="col-span-3"
              />
            </div>
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="description" className="text-right">
                Description
              </Label>
              <Textarea
                id="description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                className="col-span-3"
              />
            </div>
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="url" className="text-right">
                Website URL
              </Label>
              <Input
                id="url"
                value={url}
                onChange={(e) => setUrl(e.target.value)}
                className="col-span-3"
              />
            </div>
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="numberOfVideos" className="text-right">
                Number Of Videos
              </Label>
              <Input
                id="numberOfVideos"
                type="number"
                value={numberOfVideos}
                onChange={(e) => setNumberOfVideos(Number(e.target.value))}
                className="col-span-3"
              />
            </div>
            <div className="grid grid-cols-4 items-center gap-4">
              <Label htmlFor="interval" className="text-right">
                Interval Time Hourly
              </Label>
              <Input
                id="interval"
                type="number"
                value={interval}
                onChange={(e) => setInterval(Number(e.target.value))}
                className="col-span-3"
              />
            </div>
          </div>
          <div className="grid grid-cols-2 ">
            <Card className="overflow-hidden" x-chunk="dashboard-07-chunk-4">
              <CardHeader>
                <CardTitle>Product Demo</CardTitle>
                <CardDescription></CardDescription>
              </CardHeader>
              <CardContent>
                <div className="grid gap-2">
                  {videoURL ? (
                    <video
                      className="aspect-square w-full rounded-md object-cover"
                      height="300"
                      src={URL.createObjectURL(videoURL)}
                      width="300"
                    />
                  ) : (
                    <Image
                      alt="Product image"
                      className="aspect-square w-full rounded-md object-cover"
                      height="84"
                      src="/placeholder.svg"
                      width="84"
                    />
                  )}
                  <div className="grid grid-cols-3 gap-2">
                    {/* <button>
                      <Image
                        alt="Product image"
                        className="aspect-square w-full rounded-md object-cover"
                        height="84"
                        src="/placeholder.svg"
                        width="84"
                      />
                    </button> */}

                    <button className="flex aspect-square w-full items-center justify-center rounded-md border border-dashed">
                      <Label htmlFor="videoURL" className="text-right">
                        <Upload className="h-4 w-4 text-muted-foreground" />
                      </Label>
                      <Input
                        id="videoURL"
                        type="file"
                        accept="video/mp4"
                        onChange={handleVideoUpload}
                        className="hidden w-full h-full"
                      />

                      <span className="sr-only">Upload</span>
                    </button>
                  </div>
                </div>
              </CardContent>
            </Card>

            <Card className="overflow-hidden" x-chunk="dashboard-07-chunk-4">
              <CardHeader>
                <CardTitle>Product Images</CardTitle>
                <CardDescription></CardDescription>
              </CardHeader>
              {/* @ccc */}
              <CardContent>
                <div className="grid gap-2">
                  {imageURL ? (
                    <Image
                      alt="Product image"
                      className="aspect-square w-full rounded-md object-cover"
                      height="84"
                      src={URL.createObjectURL(imageURL)}
                      width="84"
                    />
                  ) : (
                    <Image
                      alt="Product image"
                      className="aspect-square w-full rounded-md object-cover"
                      height="84"
                      src="/placeholder.svg"
                      width="84"
                    />
                  )}
                  <div className="grid grid-cols-3 gap-2">
                    <button className="flex aspect-square w-full items-center justify-center rounded-md border border-dashed">
                      <Label htmlFor="imageURL" className="text-right">
                        <Upload className="h-4 w-4 text-muted-foreground" />
                      </Label>
                      <Input
                        id="imageURL"
                        type="file"
                        accept="image/png"
                        onChange={handleImageUpload}
                        className="hidden w-full h-full"
                      />

                      <span className="sr-only">Upload</span>
                    </button>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>

          <SheetFooter>
            <SheetClose asChild>
              <Dialog>
                <DialogTrigger>
                  <Button
                    type="submit"
                    onClick={handleCreateVideos}
                    disabled={open}
                  >
                    Save changes
                  </Button>
                </DialogTrigger>
                <DialogContent>
                  <DialogHeader>
                    <DialogTitle>Are you absolutely sure?</DialogTitle>
                    <DialogDescription>
                      <FeedbackUi
                        model={true}
                        description={description}
                        url={url}
                        productName={productName}
                        video={videoURL}
                        image={imageURL}
                        interval={interval}
                        numberOfVideos={numberOfVideos}
                        page={"sale"}
                      />
                    </DialogDescription>
                  </DialogHeader>
                </DialogContent>
              </Dialog>
            </SheetClose>
          </SheetFooter>
        </SheetContent>
      </Sheet>
      {/* Add Product */}
    </span>
  );
}

export default LeftDrawerSale;
