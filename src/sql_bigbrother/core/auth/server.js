const app = require("./src/app");
const config = require("./src/configs");

const PORT = config.port || 2405;

app.listen(PORT, () => {
	console.log(`🚀 Server ready on port ${PORT}`);
});
