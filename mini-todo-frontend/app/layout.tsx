"use client"

import "./globals.css";
import {SidebarInset, SidebarProvider, SidebarTrigger} from "@/components/ui/sidebar";
import {Separator} from "@/components/ui/separator";
import {Breadcrumb, BreadcrumbItem, BreadcrumbList, BreadcrumbPage} from "@/components/ui/breadcrumb";
import AppSidebar from "@/components/sidebar/app-sidebar";
import NavActions from "@/components/sidebar/nav-actions";

import {
    ArrowDown,
    ArrowUp,

    Bell,

    Copy,
    CornerUpLeft,
    CornerUpRight,
    FileText,
    GalleryVerticalEnd,

    LineChart,
    Link,

    Settings2,

    Trash,
    Trash2,

} from "lucide-react"

const data = {
    actions: [
        [
            {
                label: "Customize Page",
                icon: Settings2,
            },
            {
                label: "Turn into wiki",
                icon: FileText,
            },
        ],
        [
            {
                label: "Copy Link",
                icon: Link,
            },
            {
                label: "Duplicate",
                icon: Copy,
            },
            {
                label: "Move to",
                icon: CornerUpRight,
            },
            {
                label: "Move to Trash",
                icon: Trash2,
            },
        ],
        [
            {
                label: "Undo",
                icon: CornerUpLeft,
            },
            {
                label: "View analytics",
                icon: LineChart,
            },
            {
                label: "Version History",
                icon: GalleryVerticalEnd,
            },
            {
                label: "Show delete pages",
                icon: Trash,
            },
            {
                label: "Notifications",
                icon: Bell,
            },
        ],
        [
            {
                label: "Import",
                icon: ArrowUp,
            },
            {
                label: "Export",
                icon: ArrowDown,
            },
        ],
    ],
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {


    return (
    <html lang="en">
      <body>
      <SidebarProvider>
          <AppSidebar />
          <SidebarInset>
              <header className="flex h-14 shrink-0 items-center gap-2">
                  <div className="flex flex-1 items-center gap-2 px-3">
                      <SidebarTrigger />
                      <Separator orientation="vertical" className="mr-2 h-4" />
                      <Breadcrumb>
                          <BreadcrumbList>
                              <BreadcrumbItem>
                                  <BreadcrumbPage className="line-clamp-1">
                                      Project Management & Task Tracking
                                  </BreadcrumbPage>
                              </BreadcrumbItem>
                          </BreadcrumbList>
                      </Breadcrumb>
                  </div>
                  <div className="ml-auto px-3">
                      <NavActions actions={data.actions} />
                  </div>
              </header>
              {children}
          </SidebarInset>
      </SidebarProvider>
      </body>
    </html>
  );
}


