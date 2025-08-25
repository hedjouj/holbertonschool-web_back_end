<<<<<<< HEAD
import Building from 5-building.js

export default class SkyHighBuilding {
constructor(sqft, floors)
=======
import Building from './5-building';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this.floors = floors;
  }

  get floors() {
    return this._floors;
  }

  set floors(value) {
    if (typeof value !== 'number') {
      throw new Error('Floors must be a number');
    }
    this._floors = value;
  }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this._floors} floors`;
  }
>>>>>>> 7dcaf23edbac24f74c34af8b743e92f02b64b0ff
}