<template>
	<view>
		<view class = "container">
			<view style="margin-top: 5%;text-align: left;width: 100%;">
				<text style="margin-left: 25px;font-size: 20px;">Profile Photo</text>
				<view class="divider"/>
				<view class="demo-layout bg-purple-dark">
					<image :src="avatar" class="head-img">
					<u-button style="background-color: #F5C979;color: white;height: 60rpx; width: 250rpx; margin-top: 10%;margin-right: 10%; float: right;" @click="photo" >Channge Photo</u-button>
				</view>
			</view>
			
			<view style="margin-top: 10%;text-align: left;width: 100%;">
				<text style="margin-left: 25px;font-size: 20px;">Display Name</text>
				<view class="divider"/>
				<view style="margin-top: 3%; text-align: center;">
					<u-input style="width: 80%;font-weight: 900;display: inline-block;background-color: #F3F1F1;border-radius: 10px;" placeholder="Name" v-model="iName" class="fn-input" height="90" input-align="center" :clearable="false"/>
				</view>
			</view>
			
			<view style="margin-top: 10%;text-align: left;width: 100%;">
				<text style="margin-left: 25px;font-size: 20px;">Gender</text>
				<view class="divider"/>
				<radio-group style="margin-left: 4%;"@change="radioChange">
					<label class="uni-list-cell uni-list-cell-pd" v-for="(item, index) in sex" :key="item.value">
						<radio :value="item.value" :checked="index===iGender" /><span>{{item.label}}</span>
					</label>
				</radio-group>
			</view>
			
			<view style="margin-top: 10%;text-align: left;width: 100%;">
				<text style="margin-left: 25px;font-size: 20px;">Location</text>
				<view class="divider"/>
				<view style="margin-top: 3%; text-align: center; margin-left:4%; center; margin-right:4%;">
                    <view style="text-align: left;width: 100%;margin-top: 15px;">
                    	<view v-model="iSuburb" style="float: left;width: 30%;font-weight: 900;display: inline-block;background-color: #F3F1F1;border-radius: 10px;">
                    		<xfl-select @change="getSuburb"
                    			:list="suburbOptions"
                    			:clearable="false"
                    			:showItemNum="5" 
                    			:listShow="false"
                    			:isCanInput="false"  
                    			:style_Container="'height: 50px; font-size: 16px;'"
                    			:placeholder="iSuburb"
                    			:selectHideType="'hideAll'"
                    			style="width: 100%;background-color: #F3F1F1;"
                    		>
                    		</xfl-select>
                    	</view>
                    </view>
                    
                    <view style="text-align: left;width: 100%;margin-top: 15px;">
                    	<view v-model="iCity" style="float: left;width: 30%;font-weight: 900;display: inline-block;background-color: #F3F1F1;border-radius: 10px;">
                    		<xfl-select @change="getCity"
                    			:list="cityOptions"
                    			:clearable="false"
                    			:showItemNum="5" 
                    			:listShow="false"
                    			:isCanInput="false"  
                    			:style_Container="'height: 50px; font-size: 16px;'"
                    			:placeholder="iCity"
                    			:selectHideType="'hideAll'"
                    			style="width: 100%;background-color: #F3F1F1;"
                    		>
                    		</xfl-select>
                    	</view>
                    </view>
                    
                    <view style="text-align: left;width: 100%;margin-top: 15px;">
                    	<view v-model="iState" style="float: left;width: 30%;font-weight: 900;display: inline-block;background-color: #F3F1F1;border-radius: 10px;">
                    		<xfl-select @change="getState"
                    			:list="stateOptions"
                    			:clearable="false"
                    			:showItemNum="5" 
                    			:listShow="false"
                    			:isCanInput="false"  
                    			:style_Container="'height: 50px; font-size: 16px;'"
                    			:placeholder="iState"
                    			:selectHideType="'hideAll'"
                    			style="width: 100%;background-color: #F3F1F1;"
                    		>
                    		</xfl-select>
                    	</view>
                    </view>
					
				</view>
			</view>
			
			<view>
				<u-button style="background-color: #F5C979; height: 75rpx; color: white; margin-right:10%;width: 240rpx; margin-top: 10%;" @click="save">Save</u-button>
			</view>
		</view>
		<!-- #ifdef APP-PLUS -->
		<u-tabbar :list="tabbar" :mid-button="false" height="55px"></u-tabbar>
		<!-- #endif -->
		
		<!-- #ifdef H5 -->
		<u-tabbar :list="tabbar" :mid-button="false"></u-tabbar>
		<!-- #endif -->
	</view>
</template>

<script>
	export default {
		data() {
			return {
				tabbar: this.$store.state.tabbar,
				avatar: "",
				stateObject:{
					"India": { 
						"Delhi": ["new Delhi", "North Delhi"],
						"Kerala": ["Thiruvananthapuram", "Palakkad"],
						"Goa": ["North Goa", "South Goa"],
					},
					"Australia": {
						"South Australia": ["Dunstan", "Mitchell"],
						"Victoria": ["Altona", "Euroa"]
					}, 
					"Canada": {
						"Alberta": ["Acadia", "Bighorn"],
						"Columbia": ["Washington", ""]
					}
				},
				iCity:"",
                iSuburb:"",
				iState:"",
				iName:"",
				iGender:"",
				sex: [{
					label: "Female",
					value: 0,
					checked: true
				}, {
					label: "Male",
					value: 1
				},
				{
					label: "Neutral",
					value: 2
				},
				{
					label: "Unspecify",
					value: 3
				}],
				addressData: {
					sex: 3,
				},
                suburbOptions: ['Sydney', 'Redfern', 'Darlinghurst', 'Haberfield', 'Alexandria', 'Haymarket', 'Chippendale', 'Barangaroo', 'Beaconsfield', 'Chinatown', 'East Sydney', 'Elizabeth Bay', 'Erskineville', 'Eveleigh', 'Forest Lodge', 'Kings Cross', 'Millers Point', 'Potts Point', 'Pyrmont', 'Rosebery', 'Rushcutters Bay', 'Saint Peters', 'Surry HillsThe Glebe', 'The Rocks', 'Ultimo', 'Woolloomooloo', 'Zetland'],
                cityOptions: ['Sydney'],
                stateOptions: ['NSW'],
			}
		},
		onLoad(){
			this.getAvatar()
			this.loadInfo()
		},
		onShow(){
			this.getAvatar()
			this.loadInfo()
		},
		methods: {
            getCity(city){
                this.iCity = city.newVal;
            },
            getSuburb(suburb){
                this.iSuburb = suburb.newVal;
            },
            getState(state){
                this.iState = state.newVal;
            },
			getAvatar(){
				let that =this
				uni.request({
				url: "http://8.210.113.176:8080/users/avatar/"+uni.getStorageSync('userId'),
				method: 'get',
				}).then(res=>{
					console.log('res',res)
					if(res[1].data!=''){
						that.avatar = res[1].data
					}else{
						that.avatar = "../../static/girl.png"
					}
				})
			},
			photo(){
				uni.chooseImage({
				    count: 1, 
				    sizeType: ['original', 'compressed'], 
				    sourceType: ['album', 'camera'], 
				    success: function (res) {
				        console.log(JSON.stringify(res.tempFilePaths));
						// uni.previewImage({
						//     urls: res.tempFilePaths,
						// });
						let that = this
						uni.uploadFile({
							url: 'http://8.210.113.176:8080/users/avatar/update/'+uni.getStorageSync('userId'), 
							filePath: res.tempFilePaths[0], 
							name: 'file', 
							header: {
								'content-type': 'multipart/form-data' 
							},
							formData: {
								id: uni.getStorageSync('userId')
								// file: tempFilePath   
							},
							success: (uploadFileRes) => {
								console.log(uploadFileRes);
								uni.redirectTo({
								    url: "../edit/edit"
								});
							},
							fail: (err) => {
								console.log(err)
							}
						});
					}
				});	
			},
			loadInfo(){
				uni.request({
				url: "http://8.210.113.176:8080/users/profile/"+uni.getStorageSync('userId'),
				method: 'get',
				}).then(res=>{
					console.log('load',res[1].data)
					this.iName = res[1].data.name
					this.iGender = res[1].data.gender
					if(res[1].data.address!="None"){
						var location = res[1].data.address.split(", ")
						this.iSuburb = location[0]
						this.iCity = location[1]
						this.iState = location[2]
					}else{
						this.iSuburb = "Suburb"
						this.iCity = "City"
						this.iState = "State"
					}
					
					
				})
			},
			save(){
				var address=this.iSuburb+", "+this.iCity+", "+this.iState
				console.log("name", this.iName)
				console.log("gender", this.addressData.sex)
				console.log(address)
				uni.request({
					url:'http://8.210.113.176:8080/users/profile/update',
					method:'POST',
					data:{
						'address':address,
						'birthday':0,
						'gender':this.addressData.sex,
						'name':this.iName,
						'id':uni.getStorageSync('userId'), 
					},
					header: {
					     "Content-Type": "application/json"
					}, 
					success:function(res){
						console.log(res)
						uni.switchTab({
							url:"../profile/profile"
						})
					},	
				});
			},
			radioChange(e) {
                this.addressData.sex = this.radio = e.detail.value
				console.log(this.addressData.sex)
            },
			
		}
	}
</script>

<style>
	page{
		background-color: #B0C07A;
	}
	.section{
		margin-top: 5%;
		margin-left:3%;
		text-align: left;
	}
	.container{
		width: 90%;
		height: 1200rpx;
		background-color: white;
		margin-top: 7%;
		margin-left: 5%;
		border-radius: 10px;
		display: flex;
		flex-direction: column;
	}
	.divider{
		 background: #E0E3DA;
		 margin-top: 1%;
		 margin-left: 3%;
		 margin-bottom: 3%;
		 width: 95%;
		 height: 5rpx;
	}
	.head-img{
		width: 160rpx;
		height: 160rpx;
		margin-left:10%;
		border-radius: 50%;
/* 		margin-top: 5%; */
	}
</style>
