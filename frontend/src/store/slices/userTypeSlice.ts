import {createSlice} from "@reduxjs/toolkit";

const userTypeSlice = createSlice({
    name: "userType",
    initialState: {
        userType: {
            type: 'unknown',
            humanaizedType: 'unknown'
        }
    },
    reducers: {
        setUserType(state, action){
            state.userType.type = action.payload.type
            state.userType.humanaizedType = action.payload.humanaizedType
        }
    }
})

export const {setUserType} = userTypeSlice.actions

export default userTypeSlice.reducer