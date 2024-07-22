/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./product/templates/**/*.html",
        "./customer/templates/**/*.html",
        "./cart/templates/**/*.html",
        "./order/templates/**/*.html",
        "./templates/**/*.html",
        "./base_templates/**/*.html",
        "./node_modules/flowbite/**/*.js",
    ],
    theme: {
        extend: {},
    },
    plugins: [require("flowbite/plugin")],
};
