<script>
	export default {
		onLaunch: function() {
			console.log('App Launch')
			var info = plus.push.getClientInfo()
			plus.push.addEventListener("click", function(msg) {
				console.log("click:" + JSON.stringify(msg));
				console.log(msg.payload);
				console.log(JSON.stringify(msg));
				setTimeout(() => {
					if (typeof uni.getStorageSync('userId') != 'undefined' && uni.getStorageSync('userId') != '' && uni.getStorageSync('userId')){
						uni.navigateTo({
							url: `/pages/notification/notification`
						})
					}
				}, 1000)
			}, false);  
			plus.push.addEventListener("receive", function(msg) {
				console.log("recevice:" + JSON.stringify(msg))
			}, false);
			console.log('push')
			if (typeof uni.getStorageSync('userId') != 'undefined' && uni.getStorageSync('userId') != '' && uni.getStorageSync('userId')){
				uni.switchTab({
					url:'./pages/home/home'
				})
			}
			// // #ifdef APP-PLUS 
			// const _self = this;  
			// const _handlePush = function(message) {  
			// 	console.log(message);
			// 	uni.navigateTo({  
			// 		url: './pages/notification/notification'
			// 	});
			// };
			// plus.push.addEventListener('click', _handlePush);  
			// plus.push.addEventListener('receive', _handlePush);  
			// // #endif 
			
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style lang="scss">
	/*每个页面公共css */
	@import "uview-ui/index.scss";
	@import "./font/ifont.css";  
</style>
