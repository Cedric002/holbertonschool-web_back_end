import { uploadPhoto, createUser } from "./utils";

function handleProfileSignup() {
  const promises = [uploadPhoto(), createUser()];

  Promise.all(promises)
    .then(([photoResult, userResult]) => {
      const { body, firstName, lastName } = userResult;
      console.log(
        `Body: ${body}, First Name: ${firstName}, Last Name: ${lastName}`
      );
    })
    .catch((error) => {
      console.error("Signup system offline");
    });
}

export default handleProfileSignup;
