"use client"

import {SidebarMenu, SidebarMenuButton, SidebarMenuItem} from "@/components/ui/sidebar";
import {type LucideIcon} from "lucide-react"

export default function NavMain({
                     items,
                 }: {
    items: {
        title: string
        url: string
        icon: LucideIcon
        isActive?: boolean
    }[]
}) {
    return (
        <SidebarMenu>
            {items.map((item) => (
                <SidebarMenuItem key={item.title}>
                    <SidebarMenuButton asChild isActive={item.isActive}>
                        <a href={item.url}>
                            <item.icon />
                            <span>{item.title}</span>
                        </a>
                    </SidebarMenuButton>
                </SidebarMenuItem>
            ))}
        </SidebarMenu>
    )
}