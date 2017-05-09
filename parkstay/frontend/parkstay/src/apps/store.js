import Vuex from 'vuex'
import Vue from 'vue'

Vue.use(Vuex)
import {
    $,
    api_endpoints
} from '../hooks'
var store = new Vuex.Store({
    state: {
        alert:{
            visible:false,
            type:"danger",
            message: ""
        },
        regions:[],
        parks:[],
        districts:[],
        campgrounds:[],
        campsite_classes:[]
    },
    mutations: {
        SETALERT(state, a) {
            state.alert = a;
        },
        SETREGIONS(state, regions) {
            state.regions = regions;
        },
        SETPARKS(state, parks) {
            state.parks = parks;
        },
        SETDISTRICTS(state, districts) {
            state.districts = districts;
        },
        SETCAMPGROUNDS(state,campgrounds){
            state.campgrounds = campgrounds;
        },
        SETCAMPSITECLASSES(state,campsite_classes){
            state.campsite_classes = campsite_classes;
        }
    },
    actions: {
        updateAlert(context,payload) {
            context.commit('SETALERT',payload);
        },
        fetchRegions(context) {
            $.get(api_endpoints.regions,function(data){
                context.commit('SETREGIONS',data);
            });
        },
        fetchParks(context) {
            $.get(api_endpoints.parks,function(data){
                context.commit('SETPARKS',data);
            });
        },
        fetchDistricts(context) {
            $.get(api_endpoints.districts,function(data){
                context.commit('SETDISTRICTS',data);
            });
        },
        fetchCampgrounds(context){
            $.get(api_endpoints.campgrounds,function(data) {
                context.commit('SETCAMPGROUNDS',data);
            });
        },
        fetchCampsiteClasses(context){
            $.get(api_endpoints.campsite_classes,function(data){
                context.commit('SETCAMPSITECLASSES',data);
            });
        }
    },
    getters:{
        showAlert: state => {
            return state.alert.visible;
        },
        alertType: state => {
            return state.alert.type;
        },
        alertMessage: (state) =>  {
            return state.alert.message;
        },
        regions: state => {
            return state.regions;
        },
        parks: state => {
            return state.parks;
        },
        districts: state => {
            return state.districts;
        },
        campgrounds: state => {
            return state.campgrounds;
        },
        campsite_classes: state => {
            return state.campsite_classes;
        }
    }
});

export default store;
