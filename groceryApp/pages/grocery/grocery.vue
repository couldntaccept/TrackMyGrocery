<template>
	<view>
		<hx-navbar ref="hxnb" :config="config" @clickBtn="onClickBtn">
		</hx-navbar>
		<view v-if="addItemToList">
			<view class="content" >
				<view>
					<text :class="['selected-item',iisSelect?'selected-item':'un-select-item']" @click="changeTab('is')">In Stock</text>
					<text style="padding: 0 5px 0 5px;">|</text>
					<text :class="[issSelect?'selected-item':'un-select-item']" @click="changeTab('hs')">History</text>
				</view>
			</view>
			<view class="content" v-if="iisSelect">
				<view class="stock-card">
					<view>
						<u-row gutter="16" justify="space-between">
							<u-col span="6">
								<view class="demo-layout bg-purple">
									<text style="font-weight: 900;">Expiring  Products</text>
								</view>
							</u-col>
							<u-col span="5" style="text-align: right;">
								<view class="demo-layout bg-purple-light">
									<view style="text-align: center;">
										<xfl-select @change="selectSortingItemList"
											:list="sortingMethod"
											:clearable="false"
											:showItemNum="5" 
											:listShow="false"
											:isCanInput="false"  
											:style_Container="'height: 30px; font-size: 15px;'"
											:placeholder = "'Recent Added'"
											:selectHideType="'hideAll'"
											style="width: 100%; background-color: #FFFFFF;"
										>
										</xfl-select>
									</view>
									
								</view>
							</u-col>
						</u-row>
					</view>
					<view style="margin-top: 5px;">
						<u-row gutter="16" justify="space-between">
							<u-col span="6">
								<view class="demo-layout bg-purple">
									<text>Item Name</text>
								</view>
							</u-col>
							<u-col span="6" style="text-align: right;">
								<view class="demo-layout bg-purple-light">
									<text>Expiring Date</text>
										
								</view>
							</u-col>
						</u-row>
					</view>
					<view style="margin-top: 5px;">
						<block v-for="(item,index) in stockList">
							<view style="margin-top: 10px;" @click="edit(item, index)">
								
								<u-row gutter="16">
									<u-col span="3">
										<view class="demo-layout bg-purple">
											<image :src="item.img" style="width: 65px;height: 65px;">
										</view>
									</u-col>
									<u-col span="6">
										<view class="demo-layout bg-purple-light">
											<u-row gutter="18" justify="space-between">
											<text>{{ item.name }}</text>
											<view style="text-align: right;">
												<image v-if="!item.potential" src="../../static/heart-line.png" style="height: 50rpx; width: 50rpx; float:right;  margin-right: 6%;" @click.stop="saveList(item.itemId)"></image>
												<image v-if="item.potential" src="../../static/heart-fill.png" style="height: 50rpx; width: 50rpx; float:right;  margin-right: 6%;" @click.stop="deleteList(item.itemId)"></image>
											</view>	
											</u-row>
											<view>
												<u-row gutter="18" justify="space-between">
													<u-col span="4" style="text-align: left;">														
													</u-col>
													<u-col span="6" style="text-align: right;">	
																	
														<view class="demo-layout bg-purple-light" >														
															<u-button shape="circle" size="mini" style="background-color: #F3F1F1; " @click="changeAmount(index)">consume</u-button>
														</view>
													</u-col>
												</u-row>
												
												
											</view>
										</view>
									</u-col>
									<u-col span="3">
										<view class="demo-layout bg-purple-dark">
											<view class="demo-layout bg-purple">
												<text style="font-weight: 900;float:right;">{{item.expDate}}</text>
											</view>
											<text style="font-size:12px;">Remind before {{ item.time }} Days</text>
											<!-- <view>5 Days</view> -->
										</view>
									</u-col>
								</u-row>
							</view>
							<u-divider half-width="60%"></u-divider>
						</block>
					</view>
				</view>
			</view>

<!--  -->
<!--  -->
<!--  -->
			<hqs-popup title="" :from="popFrom" v-model="itemEditor" :round="round" :showClose="false" height="600px">
				<view class="t-bg">

					<view style="text-align: left;width: 100%;">
						<text style="margin-left: 25px;font-size: 20px;">Name</text>
						<view style="text-align: center;">
							<u-input style="width: 80%;font-weight: 900;display: inline-block;background-color: #F3F1F1;border-radius: 10px;" placeholder="" v-model="iName" class="fn-input" height="90" input-align="center" :clearable="false"/>
						</view>
					</view>
					
					<view style="text-align: left;width: 100%;margin-top: 15px;">
						<text style="margin-left: 25px;font-size: 20px;">Category</text>
						<view style="text-align: center;">
							<xfl-select @change="getCategory"
								:list="options"
								:clearable="false"
								:showItemNum="5" 
								:listShow="false"
								:isCanInput="false"  
								:style_Container="'height: 50px; font-size: 16px;'"
								:placeholder = "iCategory"
								:selectHideType="'hideAll'"
								style="width: 80%;background-color: #F3F1F1;"
							>
							</xfl-select>
						</view>
					</view>
					
					<view style="text-align: left;width: 100%;margin-top: 15px;">
						<text style="margin-left: 25px;font-size: 20px;">Expire Date</text>
						<view style="text-align: center;">
							<u-input @click="openTime" style="width: 80%;font-weight: 900;display: inline-block;background-color: #F3F1F1;border-radius: 10px;" :clearable="false" placeholder="Time" v-model="iTimeInAussieFormat" class="fn-input" height="90" input-align="center"/>
							<u-calendar :safe-area-inset-bottom="true" max-date="9999" v-model="cshow" @change="changeTime"></u-calendar>
						</view>
					</view>
					
					<view style="text-align: left;width: 100%;">
						<view  class="aline" style="text-align: center;">
							<text style="font-size: 20px;">Remind me</text>
							<u-input :clearable="false" style="margin-left: 5px; margin-right: 5px; width: 10px; font-weight: 900;display: inline-block;background-color: #F3F1F1;border-radius: 10px;" placeholder="" v-model="iCitime" class="fn-input" height="90" input-align="center"/>
							<text style="font-size: 20px;">days before</text>
						</view>
					</view>
					
					<view style="text-align: left;width: 100%;">
						<text style="margin-left: 25px;font-size: 20px;">Other details</text>
						<view style="text-align: center;">
							<u-input :clearable="false" style="width: 80%;font-weight: 900;display: inline-block;background-color: #F3F1F1;border-radius: 10px;" placeholder="details" v-model="iDetails" class="fn-input" height="90" input-align="center"/>
						</view>
					</view>

					<u-row gutter="16">
						<u-col span="3" style="text-align: left;float:left">
							<view style="margin-top: 20px;">
								<u-button shape="circle" :hair-line="false" style="width: 150px;background-color: #F5C979;border-color: #F5C979;" @click="changePhoto">Change photo</u-button>
							</view>
						</u-col>
						<u-col span="3" style="text-align: right;float:right">
							<view style="margin-top: 20px;margin-left: 120%;">
								<u-button shape="circle" :hair-line="false" style="width: 150px;background-color: #F5C979;border-color: #F5C979;" @click="editClient">Save</u-button>
							</view>
						</u-col>
					</u-row>				
									
									
									
									
									
									
									
				</view>
			</hqs-popup>
			
<!-- 	
<!--  -->	
<!--  -->	
			
			<hqs-popup  title="" :from="popFrom" v-model="chNum" :round="round" :showClose="false" height="300px">
				<view class="t-bg">
					<text style="font-size: 20px;font-weight: 900;">Have you consumed already？</text>
					<view class="sm-ipbox">
						<!-- <text>-</text> -->
						<!-- <view style="margin-top: 10px;font-size: 20px;margin-right: 15px;" @click=" packs-= 1">-</view>
						<u-input style="font-weight: 900;display: inline-block;background-color: #F3F1F1;border-radius: 10px;" placeholder="Amount" v-model="packs"  class="fn-input" height="90" input-align="center"/>
						<view class="sum-item" @click=" packs+= 1">+</view> -->
					</view>
					<view style="margin-top: 30px;">
						<u-button shape="circle" :hair-line="false" style="width: 130px;background-color: #F5C979;border-color: #F5C979;" @click="consume('yes')">Yes</u-button>
						<u-button shape="circle" :hair-line="false" style="width: 130px;background-color: #F5C979;border-color: #F5C979;margin-top: 10px;" @click="consume('no')">No</u-button>
					</view>
				</view>
			</hqs-popup>
			<view class="content" v-if="issSelect">
				<view class="stock-card">
					<view style="margin-top: 5px;">
						<block v-for="(item,index) in oldstockList">
							<view style="margin-top: 10px;">
								<u-row gutter="16">
									<u-col span="3">
										<view class="demo-layout bg-purple">
											<image :src="item.img" style="width: 65px;height: 65px;">
										</view>
									</u-col>
									<u-col span="6">
										<view class="demo-layout bg-purple-light">
											<text>{{ item.name }}</text>
											
											<view>
												<image v-if="!item.potential" src="../../static/heart-line.png" style="height: 50rpx; width: 50rpx; float:right;  margin-right: 6%;" @click.stop="saveList(item.itemId)"></image>
												<image v-if="item.potential" src="../../static/heart-fill.png" style="height: 50rpx; width: 50rpx; float:right;  margin-right: 6%;" @click.stop="deleteList(item.itemId)"></image>
												<!-- <text style="font-weight: 900;">{{ item.packs }}packs</text> -->
												
											</view>
										</view>
									</u-col>
									<u-col span="3">
										<view class="demo-layout bg-purple-dark">
											<view><text style="font-size: 14px;">{{ item.expDate }}</text></view>
											<view v-if="item.status=='consume'"><text style="font-size: 12px;">consumed in {{ item.conDate }}</text></view>
											<view v-if="item.status=='consume'" style="color: #FFA451;">{{item.status}}</view>
											<view v-if="item.status=='expire'" style="color: #AA4A44;">{{item.status}}</view>
										</view>
									</u-col>
								</u-row>
							</view>
							<u-divider half-width="60%"></u-divider>
						</block>
					</view>
				</view>
			</view>
		</view>
		<view v-if="needAddItem" class="content">
			<view class="" style="width: 80%;margin-top: 15px;text-align: center;">
				<u-row gutter="16" justify="space-between">
					<u-col span="3" style="text-align: left;">
						<view class="demo-layout bg-purple" >
							<u-button shape="circle" size="mini" style="background-color:black;color: white;" @click="cancelAddCard">< Cancel</u-button>
						</view>
					</u-col>
					<u-col span="3" style="text-align: right;">
						<view class="demo-layout bg-purple-light">
							<u-button shape="circle" size="mini" style="background-color: black;color: white;" @click="saveClient">Save</u-button>
						</view>
					</u-col>
				</u-row>
			</view>

		</view>
		<view class="add-card-item" v-if="needAddItem">
			<view style="text-align: left;width: 100%;">
				<text style="margin-left: 25px;font-size: 20px;">Name</text>
				<view style="text-align: center;">
					<u-input style="width: 80%;font-weight: 900;display: inline-block;background-color: #F3F1F1;border-radius: 10px;" placeholder="Name" v-model="iName" class="fn-input" height="90" input-align="center" :clearable="false"/>
				</view>
			</view>
			
			<view style="text-align: left;width: 100%;margin-top: 15px;">
				<text style="margin-left: 25px;font-size: 20px;">Category</text>
				<view style="text-align: center;">
					<xfl-select @change="getCategory"
						:list="options"
						:clearable="false"
						:showItemNum="5" 
						:listShow="false"
						:isCanInput="false"  
						:style_Container="'height: 50px; font-size: 16px;'"
						:placeholder = "'Choose'"
						:selectHideType="'hideAll'"
						style="width: 80%;background-color: #F3F1F1;"
					>
					</xfl-select>
				</view>
			</view>
			
			<view style="text-align: left;width: 100%;margin-top: 15px;">
				<text style="margin-left: 25px;font-size: 20px;">Expire Date</text>
				<view style="text-align: center;">
					<u-input @click="openTime" style="width: 80%;font-weight: 900;display: inline-block;background-color: #F3F1F1;border-radius: 10px;" :clearable="true" placeholder="Time" v-model="iTime" class="fn-input" height="90" input-align="center"/>
					<u-calendar v-model="cshow" @change="changeTime" max-date="9999"></u-calendar>
				</view>
			</view>
			
			<view style="text-align: left;width: 100%;margin-top: 15px;">
				<view  class="aline" style="text-align: center;">
					<text style="font-size: 20px;">Remind me</text>
					<u-input :clearable="false" style="margin-left: 5px; margin-right: 5px; margin-top: 10px; width: 10px; font-weight: 900;display: inline-block;background-color: #F3F1F1;border-radius: 10px;" placeholder="" v-model="iCitime" class="fn-input" height="90" input-align="center"/>
					<text style="font-size: 20px;">days before</text>
				</view>
			</view>
			
			<view style="text-align: left;width: 100%;">
				<text style="margin-left: 25px;font-size: 20px;">Other details</text>
				<view style="text-align: center;">
					<u-input :clearable="false" style="width: 80%;font-weight: 900;display: inline-block;background-color: #F3F1F1;border-radius: 10px;" placeholder="details" v-model="iDetails" class="fn-input" height="90" input-align="center"/>
				</view>
			</view>
			
			<view style="margin-top: 20px;">
				<u-button shape="circle" :hair-line="false" style="width: 150px;background-color: #F5C979;border-color: #F5C979;" @click="choosePhoto">Choose a photo</u-button>
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
	import hxNavbar from "@/components/hx-navbar/hx-navbar";
	import xflSelect from '../../components/xfl-select/xfl-select.vue'; 
	export default {
		components: {hxNavbar},
		data() {
			return {
				tabbar: this.$store.state.tabbar,
				filepath:'',
				iisSelect: true,
				iTime: '',
				iTimeInAussieFormat: '',
				itemEditor: false,
				cshow: false,
				chNum: false,
				issSelect: false,
				popFrom: 'bottom',
				packs: 0,
				round: 20,
				needChangeItem: '',
				addItemToList: true,
				needAddItem: false,
				iDetails: '',
				iCitime: '',
				iName: '',
				iItemid: '',
				status:'instock',
                iCategory: '',
				shopList:[],
				oldstockList: [],
				stockList:[],
				config:{
					title: 'Grocery',
					color: 'black',
					backgroundColor: '#B0C07A',
					back: false,
	
					statusBarBackground:'#B0C07A',
					rightButton:[{
						key: 'scan',
						icon: '&#xe62c;',
						position: 'left'
					}],
					leftButton: [{
						key: 'add',
						icon: '&#xe603;',
						position: 'left'
					}],
				},
				options: ['Fruit','Vegetable','Dairy','Animal product','Frozen','Canned Goods','Frozen Foods','Deli','Others'],
				sortingMethod: ['Recent Added', 'A-z', 'Expire Soon'],
			}
		},
		onLoad(){
			console.log(uni.getStorageSync('userId'))
			this.getCol()
			// setInterval(() => {
			// 	this.getCol()
			// },1000)
			
		},
		onShow(){
			this.getCol()
		},
		methods: {
			
			change(data){
				console.log(data.index);
				console.log(data.value);
			},
            getCategory(category){
                this.iCategory = category.newVal;
            },
            
			saveClient(){
				var date = new Date();
				
				var nowMonth = date.getMonth() + 1;
				
				var strDate = date.getDate();
				
				var seperator = "-";
				
				if (nowMonth >= 1 && nowMonth <= 9) {
				   nowMonth = "0" + nowMonth;
				}
				
				if (strDate >= 0 && strDate <= 9) {
				   strDate = "0" + strDate;
				}
				// var nowDate = date.getFullYear() + seperator + nowMonth + seperator + strDate;
                
                // convert remind time to correct form
                var expDate = new Date(this.iTime);
				var remindTime = (expDate.getDate() - this.iCitime);
				var lsRemindTime = new Date(expDate.setDate(remindTime)).toLocaleDateString().split("/");
				console.log(remindTime);
				console.log(lsRemindTime);

                //China Timezone needed
                // if(lsRemindTime[2].length === 1){
                //     lsRemindTime[2] = "0" + lsRemindTime[2]
                // }
                //Australian Timezone needed
				console.log(new Date())
                if(lsRemindTime[1].length === 1){
                    lsRemindTime[1] = "0" + lsRemindTime[1]
                }
                var remindTime = lsRemindTime[2]+"-"+lsRemindTime[0]+"-"+lsRemindTime[1]
				console.log(remindTime);
				console.log(lsRemindTime);
                this.tab(this.iTime,date);
				let item = {
				  "addDate": new Date(),
				  "addMethod": "manual",
				  "category": this.iCategory,
				  "conDate": 0,
				  "detail": this.iDetails,
				  "expDate": this.iTime,
				  "itemId": 0,
				  "name": this.iName,
				  "remindTime": remindTime,
				  "status": this.status,
				  "otherDetail": this.iDetails,
				  "uid": uni.getStorageSync('userId')
				}
				let that=this
				uni.request({
					method:'POST',
					url:'http://8.210.113.176:8080/item/insert',
					data:JSON.stringify(item)
				}).then(res => {
					console.log(that.filepath)
					console.log(res[1].data)
					uni.uploadFile({
						url: 'http://8.210.113.176:8080/item/update/picture', 
						filePath: that.filepath[0], 
						name: 'picture', 
						header: {
							'content-type': 'multipart/form-data' 
						},
						formData: {
							id: res[1].data
							// file: tempFilePath   
						},
						success: (uploadFileRes) => {
							console.log(uploadFileRes);
						},
						fail: (err) => {
							console.log(err)
						}
					});
					
				})
				this.needAddItem = false
				this.addItemToList = true

				setTimeout(() => {
					this.getCol()
				},1000)
			},
			
            
			getCol(){
				
				// if (uni.getStorageSync('userId')){
					
				// }
				
				uni.request({
					url:'http://8.210.113.176:8080/item/user/'+uni.getStorageSync('userId')
				}).then(res => {
					console.log(res[1].data)
					this.getList()
					this.updateItemList(res[1].data)
				})
			},
			
			getList(){
				uni.request({
				url: "http://8.210.113.176:8080/potential/"+uni.getStorageSync('userId'),
				method: 'get',
				}).then(res=>{
					console.log('load',res[1].data)
					this.shopList = res[1].data
				})
			},
			updateItemList(itemList){
				let stockList = []
                let oldstockList = []
				for (var i=0;i<itemList.length;i++){
                    var item = itemList[i]
					var exp = new Date(item.expDate.substr(0,10))
					var remind = new Date(item.remindTime.substr(0,10))
					// this.getImgById(item.itemId)
					var temp = item.picture
					console.log("img", item.picture)
					if(temp==null){
						temp = "../../static/stock-icon.png"
					}
					var itemInfo = {
                        "addDate": item.addDate,
                        "addMethod": item.addMethod,
                        "category": item.category,
                        "conDate": item.conDate.substr(0,10),
                        "detail": item.detail,
                        "expDate": item.expDate.substr(0,10),
                        "itemId": item.itemId,
						"img":temp,
                        "name": item.name,
                        "remindTime": item.remindTime,
                        "status": item.status,
						"time":this.DateDiff(remind,exp),
						"potential": item.potential,
                        "uid": uni.getStorageSync('userId')
					}
					
					if (itemList[i].status === 'instock'){
						stockList.push(itemInfo)
					}else{
						oldstockList.push(itemInfo)
					}
					
				}
				console.log(stockList)
				console.log(this.oldstockList)
				this.stockList = stockList
                this.oldstockList = oldstockList
				console.log(this.stockList)
			},
			
			consumeItem(item){
				let itemUpdated = {
				  "addDate": item.addDate,
				  "addMethod": item.addMethod,
				  "category": item.category,
				  "conDate": new Date(),
				  "detail": item.detail,
				  "expDate": item.expDate,
				  "itemId": item.itemId,
				  "name": item.name,
				  "remindTime": item.remindTime,
				  "status": "consume",
				  "uid": uni.getStorageSync('userId')
				}
				
				uni.request({
					method:'POST',
					url:'http://8.210.113.176:8080/item/update',
					data:JSON.stringify(itemUpdated)
				}).then(res => {
					console.log(res)
					this.getCol()
				})
			},

			changeTime(e){
				this.iTime = e.result
				var array = this.iTime.split('-')
				this.iTimeInAussieFormat = array[2]+"-"+array[1]+"-"+array[0]
				console.log(this.iTimeInAussieFormat)
				console.log(this.iTime)
                
			},
			openTime(){
				this.cshow = true
			},
			changeTab(e){
				if (e === 'is'){
					this.issSelect = false
					this.iisSelect = true
				}else if(e === 'hs'){
					this.iisSelect = false
					this.issSelect = true
				}
			},
			changeAmount(e){
				this.packs = parseInt(this.stockList[e].packs)
				this.chNum = true
				this.needChangeItem = e
			},
			consume(e){
				var changedItem = this.stockList[this.needChangeItem]
				var lsConsumeTime = new Date().toLocaleDateString().split("/");
                //China Timezone needed
                // if(lsConsumeTime[2].length === 1){
                //     lsConsumeTime[2] = "0" + lsConsumeTime[2]
                // }
				//Australian Timezone needed
                if(lsConsumeTime[1].length === 1){
                    lsConsumeTime[1] = "0" + lsConsumeTime[1]
                }
				var consumeTime = lsConsumeTime[2]+"-"+lsConsumeTime[0]+"-"+lsConsumeTime[1]
				changedItem.conDate = consumeTime
                
				if (e === 'yes'){
					this.consumeItem(changedItem)
					console.log(changedItem)
					console.log(changedItem.itemId)
                    
                    
					uni.request({
						url: 'http://8.210.113.176:8080/item/update/status/'+"consume"+"/id/"+changedItem.itemId,
					}).then(res => {
						this.getCol()
						console.log(res[1])
					})
				}
				this.chNum = false
				
			},
            
            scanPhoto(){
				let that = this
                uni.chooseImage({
                    count: 1, 
                    sizeType: ['original', 'compressed'], 

                    sourceType: ['camera', 'album'], 

                    success:  (res) => {
                        console.log(String(res.tempFilePaths[0]));
						uni.previewImage({
							urls: res.tempFilePaths,
						});
						uni.uploadFile({
							url: 'http://43.134.41.74:8080/ocr', // ------------------- 每次测之前改一下 ------------------------
							method : 'POST',
							// filePath : res.tempFilePaths[0],
							filePath : String(res.tempFilePaths[0]),
							name : 'media',
							header: {
								'content-type': 'multipart/form-data' 
							},
							
							success: (uploadFileRes) => {
								console.log("上传了: " + String(res.tempFilePaths[0]) + "  --------")
								console.log("ocr 的返回结果：");
								console.log(uploadFileRes.data);

								that.iTime = uploadFileRes.data;
								console.log(that.iTime);
							},
							fail: (uploadFileRes) => {
								console.log("爷失败了");
								console.log(uploadFileRes+"\n==============");
								
							}
							
						});
                    }
                });
            },
            
			onClickBtn(e){
				if (e.key == 'add'){
					this.addItemToList = false
					this.needAddItem = true
					this.iName = '';
					this.iCategory = '';
					this.iTime = '';
					this.iCitime = '';
					this.iDetails = '';
					this.iItemid = '';
				}else{
                    this.scanPhoto()
                }
			},
            
			cancelAddCard(){
				this.needAddItem = false
				this.addItemToList = true
			},
			DateDiff(date1, date2) {
				const date1utc = Date.UTC(date1.getFullYear(), date1.getMonth(), date1.getDate());
				const date2utc = Date.UTC(date2.getFullYear(), date2.getMonth(), date2.getDate());
				var day = 1000*60*60*24;
				return (date2utc - date1utc)/day
			},
			choosePhoto(){
				let that = this
				uni.chooseImage({
				    count: 1, 
				    sizeType: ['original', 'compressed'], 
				    sourceType: ['album','camera'], 
				    success: function (res) {
				        console.log(JSON.stringify(res.tempFilePaths));
						that.filepath = res.tempFilePaths
						uni.previewImage({
							urls: res.tempFilePaths,
						});
				    }
				});
			},
			tab(date1,date2){
                console.log(date1, date2)
				// exp 1, today2
				var oDate1 = new Date(date1);
                console.log(oDate1)
				var oDate2 = new Date(date2);
                console.log(oDate2)
				if(oDate1.getTime() >= oDate2.getTime()){
					console.log('instock');
					this.status='instock';
				} else if(oDate1.getTime() < oDate2.getTime()){
					console.log('expire');
					this.status='expire';
				}
			},
			edit(item, index){
				this.itemEditor = true;
				Object.keys(item).forEach(key => {
					console.log(key, item[key]);
				});
				this.iName = item.name;
				this.iCategory = item.category;
				this.iTime = item.expDate;
				this.iCitime = item.time;
				this.iDetails = item.detail;
				this.iItemid = item.itemId;
			},
			editClient(){

					var date = new Date();
					
					var nowMonth = date.getMonth() + 1;
					
					var strDate = date.getDate();
					
					var seperator = "-";
					
					if (nowMonth >= 1 && nowMonth <= 9) {
					   nowMonth = "0" + nowMonth;
					}
					
					if (strDate >= 0 && strDate <= 9) {
					   strDate = "0" + strDate;
					}
					// var nowDate = date.getFullYear() + seperator + nowMonth + seperator + strDate;
				    
				    // convert remind time to correct form
				    var expDate = new Date(this.iTime);
				    var remindTime = (expDate.getDate() - this.iCitime); 
					var lsRemindTime = new Date(expDate.setDate(remindTime)).toLocaleDateString().split("/");
				    console.log(remindTime);
				    console.log(lsRemindTime);
					//China Timezone needed
				    // if(lsRemindTime[2].length === 1){
				    //     lsRemindTime[2] = "0" + lsRemindTime[2]
				    // }
				    //Australian Timezone needed
					console.log(new Date())
				    if(lsRemindTime[1].length === 1){
				        lsRemindTime[1] = "0" + lsRemindTime[1]
				    }
				    var remindTime = lsRemindTime[2]+"-"+lsRemindTime[0]+"-"+lsRemindTime[1]
					console.log(remindTime);
					console.log(lsRemindTime);
					this.tab(this.iTime,date);
					let item = {
					  "addDate": new Date(),
					  "addMethod": "manual",
					  "category": this.iCategory,
					  "conDate": 0,
					  "detail": this.iDetails,
					  "expDate": this.iTime,
					  "itemId": this.iItemid,
					  "name": this.iName,
					  "remindTime": remindTime,
					  "status": this.status,
					  "otherDetail": this.iDetails,
					  "uid": uni.getStorageSync('userId')
					}
					uni.request({
						method:'POST',
						url:'http://8.210.113.176:8080/item/update',
						data:JSON.stringify(item)
					}).then(res => {
						console.log(res)
					})
					this.needAddItem = false
					this.addItemToList = true
				
					setTimeout(() => {
						this.getCol()
					},1000)
					this.itemEditor = false;
					
			},
			selectSortingItemList(category){
				
				if (category.newVal === "A-z"){
					this.sortStockListAlphabetical();
				}else if (category.newVal === "Expire Soon"){
					this.sortStockListByExpDate();
				}else if (category.newVal === "Recent Added"){
					this.sortStockListByAddDate();
				}

			},
			sortStockListAlphabetical(){
				// this function will sort the stocklist by the name of each item in ascending order
				this.stockList.sort(function(a, b){
				  let dateA = a.name;
				  let dateB = b.name;
				  if (dateA < dateB){
				    return -1;
				  } else if (dateA > dateB){
				    return 1;
				  }   
				  return 0;
				});
			}
			,
			sortStockListByExpDate(){
				// this function will sort the stocklist by the expire date of each item in ascending order
				// E.g. Apple expires at 2021/Dec/12, Orange expires at 2021/Nov/11, Tofu expires at 2021/Dec/31
				// the order after sort will be Orange -> Apple -> Tofu
				this.stockList.sort(function(a, b){
				  let dateA = a.expDate;
				  let dateB = b.expDate;
				  if (dateA < dateB){
				    return -1;
				  } else if (dateA > dateB){
				    return 1;
				  }   
				  return 0;
				});
			}
			,
			sortStockListByAddDate(){
				// this function will sort the stocklist by the date date of each item in ascending order
				// E.g. Apple added at 2021/Dec/12, Orange added at 2021/Nov/11, Tofu added at 2021/Dec/31
				// the order after sort will be Orange -> Apple -> Tofu
				this.stockList.sort(function(a, b){
				  let dateA = a.addDate;
				  let dateB = b.addDate;
				  if (dateA < dateB){
				    return -1;
				  } else if (dateA > dateB){
				    return 1;
				  }   
				  return 0;
				});
			},
			getImgById(id){
				uni.request({
				url: "http://8.210.113.176:8080/item/picture/"+id,
				method: 'get',
				}).then(res=>{
					console.log(res[1].data)
				})
			},
			
			saveList(id){
				uni.showLoading({title: 'updating',mask:true});
				uni.request({
				url: "http://8.210.113.176:8080/potential/add/"+id+"/"+uni.getStorageSync('userId'),
				method: 'get',
				}).then(res=>{
					this.getCol()
					setTimeout(function () {uni.hideLoading();}, 1000);
				})
			},
			deleteList(id){
				uni.showLoading({title: 'updating',mask:true});
				uni.request({
				url: "http://8.210.113.176:8080/potential/remove/"+id+"/"+uni.getStorageSync('userId'),
				method: 'get',
				}).then(res=>{
					this.getCol()
					setTimeout(function () {uni.hideLoading();}, 1000);
				})
			},		
			changePhoto(){
				let that = this
				uni.chooseImage({
				    count: 1, 
				    sizeType: ['original', 'compressed'], 
				    sourceType: ['album','camera'], 
				    success: function (res) {
						console.log(that.iItemid)
						uni.uploadFile({
							url: 'http://8.210.113.176:8080/item/update/picture', 
							filePath: res.tempFilePaths[0], 
							name: 'picture', 
							header: {
								'content-type': 'multipart/form-data' 
							},
							formData: {
								id: that.iItemid
								// file: tempFilePath   
							},
							success: (uploadFileRes) => {
								console.log(uploadFileRes);
							},
							fail: (err) => {
								console.log(err)
							}
						});
				    }
				});
				
			}
			
		}
	}
	
</script>

<style>
	page{
		background-color: #B0C07A;
	}
	.aline{
		display: flex;
		/* justify-content: center; */
		align-items: center;
		padding: 30px;
	}
	.content{
		display: flex;
		justify-content: center;
		width: 100%;
	}
	.selected-item{
		font-size: 15px;
		font-weight: 900;
		color: black;
	}
	.un-select-item{
		font-size: 12px;
		font-weight: 300;
		color: #545b66;
	}
	.stock-card{
		width: 90%;
		/* height: 300rpx; */
		padding: 10px 10px 10px 10px;
		background-color: white;
		margin-top: 50rpx;
		border-radius: 10px;
		display: flex;
		justify-content: center;
		flex-direction: column;
		text-align: center;
	}
	.t-bg{
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
	}
	.sm-ipbox{
		margin-top: 40px;
		display: flex;
		justify-content: center;
		flex-direction: row;
		text-align: center;
		
		
		
	}
	.sum-item{
		margin-top: 10px;
		font-size: 20px;
		margin-left: 15px;
		font-weight: 1900;
	}
	.add-card-item{
		display: flex;
		justify-content: center;
		flex-direction: column;
		width: 100%;
		margin-top: 30px;
		/* text-align: center; */
		/* align-items: center; */
	}
</style>
