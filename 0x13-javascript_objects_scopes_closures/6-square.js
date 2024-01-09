#!/usr/bin/node
const Square = require('./5-square.js');

class Square extends Square {
	constructor(size) {
		super(size);
	}

	charPrint(c) {
		if (c === undefined) {
			c = 'X';
		}

		for (let i = 0; i < thi.height; i++) {
			console.log(c.repeat(this.width));
		}
	}
}
module.exports = Square;
