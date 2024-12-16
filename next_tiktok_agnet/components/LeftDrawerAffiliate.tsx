"use client";

import React, { FormEventHandler, SyntheticEvent, useState } from "react";

import { PlusCircle } from "lucide-react";

import { Input } from "@/components/ui/input";

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

function LeftDrawerAffiliate() {
  const [description, setDescription] = useState(
    "Become the Person You Dream to Be."
  );
  const [productName, setProductName] = useState("wehusstle");
  const [url, setUrl] = useState("https://wehusstle.vercel.app/");

  const [open, setOpen] = React.useState(false);

  function handleCreateVideos() {
    console.log(`${description} ${productName} ${url}`);
    setOpen(true);
  }

  return (
    <span className="sr-only sm:not-sr-only sm:whitespace-nowrap">
      <Sheet>
        <SheetTrigger asChild>
          {/* @@add_product */}
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
                Name
              </Label>
              <Input
                id="name"
                value={productName}
                className="col-span-3"
                onChange={(e) => setProductName(e.target.value)}
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
              <Label htmlFor="Website" className="text-right">
                Website
              </Label>
              <Input
                id="Website"
                value={url}
                className="col-span-3"
                onChange={(e) => setUrl(e.target.value)}
              />
            </div>
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
                        page={"affiliate"}
                      />
                    </DialogDescription>
                  </DialogHeader>
                </DialogContent>
              </Dialog>
            </SheetClose>
          </SheetFooter>
        </SheetContent>
      </Sheet>
    </span>
  );
}

export default LeftDrawerAffiliate;
