import axios from "axios"

const API = axios.create({

  baseURL:
    import.meta.env.VITE_API_URL ||

    "http://localhost:8000"
})

export const analyzeIncident = async (

  file

) => {

  const formData = new FormData()

  formData.append(
    "file",
    file
  )

  const response = await API.post(

    "/analyze",

    formData,

    {
      headers: {

        "Content-Type":
          "multipart/form-data"
      }
    }
  )

  return response.data
}