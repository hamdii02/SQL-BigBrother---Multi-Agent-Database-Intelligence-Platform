const express = require("express");
const router = express.Router();

router.use("/auth", require("./auth.route"));
router.use("/chat", require("./chat.route"));

router.get("/", (req, res, next) => {
	return res.status(200).json(`API Connected`);
});

module.exports = router;
