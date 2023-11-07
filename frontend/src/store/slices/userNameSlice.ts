import {createSlice} from "@reduxjs/toolkit";

const userNameSlice = createSlice({
    name: "userName",
    initialState: {
        userName: "Иванов Иван Иванович"
    },
    reducers: {
        setUserName(state, action){
            state.userName = action.payload
}
    }
})

export const {setUserName} = userNameSlice.actions

export default userNameSlice.reducer