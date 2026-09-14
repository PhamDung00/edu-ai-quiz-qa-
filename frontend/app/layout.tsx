import type { Metadata } from "next";
import "./globals.css";
import { Nav } from "@/components/Nav";

export const metadata: Metadata = {
  title: "EDU AI Quiz & Q&A",
  description: "AI-powered learning, quiz and Q&A platform",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="vi">
      <body>
        <Nav />
        {children}
      </body>
    </html>
  );
}
