"use client"

import {Sidebar, SidebarContent, SidebarHeader, SidebarRail} from "@/components/ui/sidebar";
import NavMain from "@/components/sidebar/nav-main";
import NavFavorites from "@/components/sidebar/nav-favorites";
import NavWorkspaces from "@/components/sidebar/nav-workspace";
import NavSecondary from "@/components/sidebar/nav-secondary";
import {
    ArrowDown,
    ArrowUp,
    AudioWaveform,
    Bell,
    Calendar,
    Command,
    Copy,
    CornerUpLeft,
    CornerUpRight,
    FileText,
    GalleryVerticalEnd,
    Home,
    LineChart,
    Link,
    MessageCircleQuestion,
    Search,
    Settings2,
    Sparkles,
    Trash,
    Trash2,
} from "lucide-react"

const data = {
    teams: [
        {
            name: "Acme Inc",
            logo: Command,
            plan: "Enterprise",
        },
        {
            name: "Acme Corp.",
            logo: AudioWaveform,
            plan: "Startup",
        },
        {
            name: "Evil Corp.",
            logo: Command,
            plan: "Free",
        },
    ],
    navMain: [
        {
            title: "Search",
            url: "#",
            icon: Search,
        },
        {
            title: "Ask AI",
            url: "#",
            icon: Sparkles,
        },
        {
            title: "Home",
            url: "#",
            icon: Home,
            isActive: true,
        },
    ],
    navSecondary: [
        {
            title: "Calendar",
            url: "#",
            icon: Calendar,
        },
        {
            title: "Settings",
            url: "#",
            icon: Settings2,
        },
        {
            title: "Trash",
            url: "#",
            icon: Trash2,
        },
        {
            title: "Help",
            url: "#",
            icon: MessageCircleQuestion,
        },
    ],
    favorites: [
        {
            name: "Project Management & Task Tracking",
            url: "#",
            emoji: "📊",
        },

    ],
    workspaces: [
        {
            name: "Personal Life Management",
            emoji: "🏠",
            pages: [
                {
                    name: "Daily Journal & Reflection",
                    url: "#",
                    emoji: "📔",
                },
                {
                    name: "Health & Wellness Tracker",
                    url: "#",
                    emoji: "🍏",
                },
                {
                    name: "Personal Growth & Learning Goals",
                    url: "#",
                    emoji: "🌟",
                },
            ],
        },
    ],
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


export default function AppSidebar({ ...props }: React.ComponentProps<typeof Sidebar>) {
    return (
        <Sidebar className="border-r-0" {...props}>
            <SidebarHeader>
                <NavMain items={data.navMain} />
            </SidebarHeader>
            <SidebarContent>
                <NavFavorites favorites={data.favorites} />
                <NavWorkspaces workspaces={data.workspaces} />
                <NavSecondary items={data.navSecondary} className="mt-auto" />
            </SidebarContent>
            <SidebarRail />
        </Sidebar>
    )
}