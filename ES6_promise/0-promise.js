export default function getResponseFromAPI() {
    const maPromesse = new Promise((resolve, reject) => {
        if (everythingisok) {
            resolve("Success");
        }
        else {
            reject("Error");
        }
    });
}
