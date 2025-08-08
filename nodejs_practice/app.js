const express = require("express");
const app = express();

const port = 3000;
app.get("/", (req, res) => {
    res
        .status(200)
        .json({ message: "Hi from server!!", app: "natours" })
})

app.listen(port, () => {
    console.log(`Your server is running on port ${port}...`)
});