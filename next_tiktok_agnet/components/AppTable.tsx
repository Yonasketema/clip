import React from "react";
import { Badge } from "@/components/ui/badge";
import { TableBody, TableCell, TableRow } from "@/components/ui/table";

import { MoreHorizontal } from "lucide-react";
import { Button } from "@/components/ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuLabel,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

import Image from "next/image";

type AppTableProps = {
  productName?: string;
  status?: boolean;
  productWebsite?: string;
  date?: string;
  description?: string;
  videoURL?: string;
};

function AppTable({
  productName,
  status,
  productWebsite,
  date,
  description,
  videoURL,
}: AppTableProps) {
  return (
    <TableBody>
      <TableRow>
        <TableCell className="hidden sm:table-cell w-44">
          <video controls width="1080" height="1920" className="w-full">
            <source type="video/mp4" src={videoURL} />
          </video>
        </TableCell>
        <TableCell className="font-medium">{productName}</TableCell>
        <TableCell>
          <Badge variant="outline">{status ? "Posted" : "Stage"}</Badge>
        </TableCell>
        <TableCell className="hidden md:table-cell">{productWebsite}</TableCell>
        <TableCell className="hidden md:table-cell">{date}</TableCell>
        <TableCell className="hidden md:table-cell">{description}</TableCell>
        <TableCell>
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button aria-haspopup="true" size="icon" variant="ghost">
                <MoreHorizontal className="h-4 w-4" />
                <span className="sr-only">Toggle menu</span>
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end">
              <DropdownMenuLabel>Actions</DropdownMenuLabel>
              <DropdownMenuItem>Edit</DropdownMenuItem>
              <DropdownMenuItem>Delete</DropdownMenuItem>
            </DropdownMenuContent>
          </DropdownMenu>
        </TableCell>
      </TableRow>
    </TableBody>
  );
}

export default AppTable;
