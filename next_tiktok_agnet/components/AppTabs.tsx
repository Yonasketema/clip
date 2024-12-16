"use client";

import React, { useState } from "react";

import { File, ListFilter } from "lucide-react";

import { Button } from "@/components/ui/button";
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Table, TableHead, TableHeader, TableRow } from "@/components/ui/table";
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs";
import AppTable from "@/components/AppTable";

type AppTabsProps = {
  result: any;
  LeftDrawer: any;
};

function AppTabs({ result, LeftDrawer }: AppTabsProps) {
  const [tabState, setTabState] = useState(result[0].productName);

  return (
    <Tabs
      defaultValue={result[0].productName}
      onValueChange={(value: string) => setTabState(value)}
    >
      <div className="flex items-center">
        <TabsList>
          {result.map((res) => (
            <TabsTrigger
              value={res.productName}
              key={res.productName}
              className="font-semibold text-2xl px-3 py-1"
            >
              {res.productName}
            </TabsTrigger>
          ))}
        </TabsList>
        <div className="ml-auto flex items-center gap-2">
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="outline" size="sm" className="h-8 gap-1">
                <ListFilter className="h-3.5 w-3.5" />
                <span className="sr-only sm:not-sr-only sm:whitespace-nowrap">
                  Filter
                </span>
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end">
              <DropdownMenuLabel>Filter by</DropdownMenuLabel>
              <DropdownMenuSeparator />
              <DropdownMenuCheckboxItem checked>
                Active
              </DropdownMenuCheckboxItem>
              <DropdownMenuCheckboxItem>Draft</DropdownMenuCheckboxItem>
              <DropdownMenuCheckboxItem>Archived</DropdownMenuCheckboxItem>
            </DropdownMenuContent>
          </DropdownMenu>
          <Button size="sm" variant="outline" className="h-8 gap-1">
            <File className="h-3.5 w-3.5" />
            <span className="sr-only sm:not-sr-only sm:whitespace-nowrap">
              Export
            </span>
          </Button>
          <Button size="sm" className="h-8 gap-1">
            {/* <PlusCircle className="h-3.5 w-3.5" /> */}
            {LeftDrawer}
          </Button>
        </div>
      </div>
      {result.map((res) => (
        <TabsContent value={res.productName}>
          <Card x-chunk="dashboard-06-chunk-0">
            <CardHeader>
              <CardTitle>Videos</CardTitle>
              <CardDescription>
                Manage your product marketing and view their sales performance.
              </CardDescription>
            </CardHeader>
            <CardContent>
              <Table>
                {/* Table Header */}
                <TableHeader>
                  <TableRow>
                    <TableHead className="hidden w-[100px] sm:table-cell">
                      <span className="sr-only">Image</span>
                    </TableHead>
                    <TableHead>ProductName</TableHead>
                    <TableHead>Status</TableHead>
                    <TableHead className="hidden md:table-cell">
                      ProductWebsite
                    </TableHead>
                    <TableHead className="hidden md:table-cell">
                      Created at
                    </TableHead>
                    <TableHead className="hidden md:table-cell">
                      Description
                    </TableHead>
                    <TableHead>
                      <span className="sr-only">Actions</span>
                    </TableHead>
                  </TableRow>
                </TableHeader>

                {/* Table Header */}
                {/* Table ROW */}
                {result
                  .reduce((shortMessages, i) => {
                    if (i.productName === tabState) {
                      shortMessages.push(...i.list);
                    }
                    return shortMessages;
                  }, [])
                  .map((cv) => (
                    <AppTable
                      key={cv.id}
                      description={cv.description || ""}
                      date={cv.createAt.toLocaleDateString()}
                      productName={cv.productName || ""}
                      productWebsite={cv.productWebsite || ""}
                      status={cv.status || false}
                      videoURL={cv.videoUrl || ""}
                    />
                  ))}
                {/* Table ROW */}
              </Table>
            </CardContent>
            <CardFooter>
              <div className="text-xs text-muted-foreground">
                Showing <strong>1-10</strong> of <strong>32</strong> products
              </div>
            </CardFooter>
          </Card>
        </TabsContent>
      ))}
    </Tabs>
  );
}

export default AppTabs;
