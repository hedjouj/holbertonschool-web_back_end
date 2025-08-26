export default function getResponseFromAPI() {
    const maPromesse = new Promise((resolve, reject) => {
        if (everythingisok) {
            resolve("True");
        }
        else {
            reject("False");
        }
    });
}
