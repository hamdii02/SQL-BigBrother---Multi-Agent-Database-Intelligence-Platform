const { BadRequestError } = require("../middlewares/error.response");
const keystoreModel = require("../models/keystore.model");

class KeyStoreService {
	static createKeyStore = async ({ userId, publicKey, privateKey, refreshToken }) => {
		const filter = { user: userId };
		const update = {
			publicKey,
			privateKey,
			refreshTokensUsed: [],
			refreshToken,
		};
		const options = { upsert: true, new: true };

		const newKeyStore = await keystoreModel.findOneAndUpdate(
			filter,
			update,
			options
		);

		if (!newKeyStore) throw new BadRequestError(`❌ Error: KeyStoreService.createToken`);

		return newKeyStore;
	};

	static findByUser = async (userId) => {
		return await keystoreModel.findOne({ user: userId });
	};

	static findByRefreshToken = async (refreshToken) => {
		const keyStore = await keystoreModel.findOne({ refreshToken });

		if (!keyStore) {
			throw new BadRequestError(`❌ Error: KeyStore Not Found!`, 404);
		}

		return keyStore;
	}

	static deleteKeyStoreById = async (keyStoreId) => {
		return await keystoreModel.deleteOne({ _id: keyStoreId });
	};

	static deleteKeyStoreByUser = async (userId) => {
		return await keystoreModel.deleteOne({ user: userId });
	}

	static deleteRefreshedKeyStore = async (refreshToken) => {
		return await keystoreModel.findOneAndDelete({ refreshTokensUsed: refreshToken}).lean();
	}
}

module.exports = KeyStoreService;
