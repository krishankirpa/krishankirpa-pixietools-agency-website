/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        brand: {
          bg: "#08090B",
          secondary: "#101216",
          surface: "#15181D",
          text: "#F5F5F3",
          muted: "#A5A9B1",
          dim: "#777D87",
          border: "rgba(255, 255, 255, 0.10)",
          glass: "rgba(255, 255, 255, 0.045)",
          gold: "#C8A96B",
          goldHover: "#DFC38C",
        },
      },
      fontFamily: {
        sans: ['Inter', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'Monaco', 'Consolas', 'monospace'],
      },
      letterSpacing: {
        widest: '0.15em',
        tightest: '-0.03em',
      },
    },
  },
  plugins: [],
};
