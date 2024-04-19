/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        "./product/templates/**/*.html", // Adicionando o diretório de templates em product/templates
        "./templates/**/*.html",
        "./base_templates/**/*.html",
        "./node_modules/flowbite/**/*.js",
    ],
    theme: {
        extend: {},
    },
    plugins: [require("flowbite/plugin")],
};
