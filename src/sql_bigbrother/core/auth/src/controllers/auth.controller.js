const { SuccessResponse } = require("../middlewares/success.response");
const AuthService = require("../services/auth.services");

class AuthController {
	/************************************* SIGN UP **********************************************
	 * @url     /api/v1/auth/signUp
	 * @method  POST
	 * @desc    signUp a new account
	 * @param   {String} username
	 * @param   {String} email
	 * @param   {String} password
	 * @param   {String} confirmPassword
	 * @param   {String} gender
	 * @return  {JSON} user, accessToken, refreshToken
	 */
	static async signUp(req, res, next) {
		const metadata = await AuthService.signUp({ ...req.body });
		return new SuccessResponse({
			code: 201,
			message: `✔️ Created new User`,
			metadata,
		}).send({
			response: res,
			callback: (res) => {
				res.cookie("accessToken", metadata.accessToken, {
					maxAge: 2 * 24 * 60 * 60 * 1000,
					httpOnly: true,
					sameSite: "strict",
					secure: process.env.NODE_ENV !== "development",
				});
			},
		});
	}

	/************************************* SIGN IN **********************************************
	 * @url     /api/v1/auth/signIn
	 * @method  POST
	 * @desc    login to account
	 * @param   {String} email
	 * @param   {String} password
	 * @return  {JSON} user, accessToken, refreshToken
	 */
	static async signIn(req, res, next) {
		const metadata = await AuthService.signIn({ ...req.body });
		return new SuccessResponse({
			code: 200,
			message: `✔️ Login Successfully`,
			metadata,
		}).send({
			response: res,
			callback: (res) => {
				res.cookie("accessToken", metadata.accessToken, {
					maxAge: 2 * 24 * 60 * 60 * 1000,
					httpOnly: true,
					sameSite: "strict",
					secure: process.env.NODE_ENV !== "development",
				});
			},
		});
	}

	/************************************* SIGN IN WITH GOOGLE **********************************************
	 * @url     /api/v1/auth/signInWithGoogle
	 * @method  POST
	 * @desc    login with google
	 * @param   {String} username
	 * @param   {String} email
	 * @param   {String} avatar
	 * @param   {String} googleId
	 * @return  {JSON} user, accessToken, refreshToken
	 */
	static async signInWithGoogle(req, res, next) {
		const metadata = await AuthService.signInWithGoogle({ ...req.body });
		return new SuccessResponse({
			code: 200,
			message: `✔️ Login Successfully`,
			metadata,
		}).send({
			response: res,
			callback: (res) => {
				res.cookie("accessToken", metadata.accessToken, {
					maxAge: 2 * 24 * 60 * 60 * 1000,
					httpOnly: true,
					sameSite: "strict",
					secure: process.env.NODE_ENV !== "development",
				});
			},
		});
	}

	/************************************* LOG OUT **********************************************
	 * @url     /api/v1/auth/logOut
	 * @method  POST
     * @headers x-client-id 
	 * @desc    logout account
	 * @return  {JSON} 
	 */
	static async logOut(req, res, next) {
		return new SuccessResponse({
			code: 200,
			message: `✔️ Logout Successfully`,
			metadata: await AuthService.logOut({ userId: req.user._id }),
		}).send({
			response: res,
			callback: (res) => {
				res.cookie("accessToken", "", {
					maxAge: 2 * 24 * 60 * 60 * 1000,
				});
			},
		});
	}
}

module.exports = AuthController;
