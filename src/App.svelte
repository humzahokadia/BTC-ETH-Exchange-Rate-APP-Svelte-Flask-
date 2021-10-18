<script>
	export let name;//get Coin names from main.js
	let bbuy1;//Crypto buy and sell prices bbuy1 = bitcoin buy price 1
	let bbuy2;
	let bsell1;//bsell1 = bitcoin sell price 1
	let bsell2;
	let ebuy1;// ebuy1 = ethereum buy price 1
	let ebuy2;
	let esell1;// esell1 = ethereum sell price 1
	let esell2;
	let bsc1;//colors for buy/sell price data bsc1 = bitcoin sell price color 1
	let bsc2;
	let bbc1;// bbc1 = bitcoin buyprice color 1
	let bbc2;
	let esc1;// esc1 = ethereum sell price color 1
	let esc2;
	let ebc1;// ebc1 = ethereum buy price color 1
	let ebc2;
	let rbbuy;//recomended site/difference price  rbbuy = recommend bitcoin buy
	let rbbd;//rbbd = recommend bitcoin buy price difference eg buy1-buy2
	let rbsell;//rbsell = recommend bitcoin sell
	let rbsd;//rbsd = recommend bitcoin buy price difference eg sell1-sell2
	let rebuy;//rebuy = recommend ethereum buy
	let rebd;//rebd = recommend ethereum buy price difference eg buy1-buy2
	let resell;//resell = recommend ethereum sell
	let resd;//resd = recommend ethereum buy price difference eg sell1-sell2
		async function getExchangedata() {//main function to get data
			let btc1 = await fetch("./btc")//call api for first BTC DATA
			.then(response => response.json())
					.then(data => {
						console.log(data);
						return data
					})
			let btc2 = await fetch("./btc2")//api for second BTC data
					.then(response => response.json())
					.then(data => {
						console.log(data);
						return data
					})
			let eth1 = await fetch("./eth")//api for first ETH data
					.then(response => response.json())
					.then(data => {
						console.log(data);
						return data
					})
			let eth2 = await fetch("./eth2")//api for second ETH data
					.then(response => response.json())
					.then(data => {
						data = data.result
						data = data.XETHZUSD
						console.log(data);
						return data
					})//gets all data in json format
			var y = btc2.USD;// parse Json data and put it into respective variables
			bsell1 = btc1.ask;
			bbuy1 = btc1.bid;
			bsell2 = y.sell;
			bbuy2 = y.buy;
			esell1 = eth1.ask;
			ebuy1 = eth1.bid;
			esell2 = eth2.a[0].slice(0, -3);//make sure decimal point is same for all numbers
			ebuy2 = eth2.b[0].slice(0, -3);
			SetColor();//set colors of prices(recomended is green other is red)/calculate which one recommend
			return JSON.stringify(eth2);

		}
		function SetColor() {//set colors and find recomendations
			if (bsell1 > bsell2){//check prices
				rbsell = "Bitfinex.com";//set recommend Source
				rbsd = bsell1 - bsell2;//set recommended source Price difference from non recommended
				rbsd = rbsd.toString().slice(0, -13);
				bsc1 = "green";//set colors
				bsc2 = "red";
			}
			else if(bsell1 == bsell2){
				rbsell = "Either";
				rbsd = 0;
				bsc1 = "green";
				bsc2 = "green";
			}
			else{
				rbsell = "Blockchain.com";
				rbsd = bsell2 - bsell1;
				rbsd = rbsd.toString().slice(0, -13);
				bsc1 = "red";
				bsc2 = "green";
			}
			if (esell1 > esell2){
				resell = "Bitfinex.com";
				resd = esell1 - esell2;
				resd = resd.toString().slice(0, -13);
				esc1 = "green";
				esc2 = "red";
			}
			else if(esell1 == esell2){
				resell = "Either";
				resd = 0;
				esc1 = "green";
				esc2 = "green";
			}
			else{
				resell = "Kraken.com";
				resd = esell2 - esell1;
				resd = resd.toString().slice(0, -13);
				esc1 = "red";
				esc2 = "green";
			}
			if (bbuy1 < bbuy2){
				rbbuy = "Bitfinex.com";
				rbbd = bbuy2 - bbuy1;
				rbbd = rbbd.toString().slice(0, -13);
				bbc1 = "green";
				bbc2 = "red";
			}
			else if(bbuy1 == bbuy2){
				rbbuy = "Either";
				rbbd = 0;
				bbc1 = "green";
				bbc2 = "green";
			}
			else{
				rbbuy = "Blockchain.com";
				rbbd = bbuy1 - bbuy2;
				rbbd = rbbd.toString().slice(0, -13);
				bbc1 = "red";
				bbc2 = "green";
			}
			if (ebuy1 < ebuy2){
				rebuy = "Bitfinex.com";
				rebd = ebuy2 - ebuy1;
				rebd = rebd.toString().slice(0, -13);
				ebc1 = "green";
				ebc2 = "red";
			}
			else if(ebuy1 == ebuy2){
				rebuy = "Either";
				rbsd = 0;
				ebc1 = "green";
				ebc2 = "green";
			}
			else{
				rebuy = "Kraken.com";
				rebd = ebuy1 - ebuy2;
				rebd = rebd.toString().slice(0, -13);
				ebc1 = "red";
				ebc2 = "green";
			}
		}
		let promise = getExchangedata();//set promise to get asyncronous data

		function handleClick() {//button onlclick
			promise = getExchangedata();//updates data
		}
</script>
<meta name="viewport" content="width=device-width, initial-scale=1"><!-- Makes page responsive for all devices -->
<main>
	<!-- project title -->
	<h1>Exchange Rate {name}</h1>
	{#await promise}
		<!-- wait for data to be fetched -->
		<p>...waiting</p><!-- wait message -->
	{:then data}<!-- do when data has been received -->
		<part1><!-- Part 1  -->
			<h2><strong>Exchange Rates Buy And Sell</strong></h2><br><!-- Display -->
			<button on:click={handleClick}><!-- update button -->
				Update Data
			</button>
			<table style="width:50%"><!-- table to hold data and headers -->
				<tr style="width:100%">
					<th style="width:25%"  colspan="4">Bitcoin</th><!-- Coin Names -->
				</tr>
				<tr style="width:100%">
					<th  style="width:50%"  colspan="2">Bitfinex.com</th><!-- Exchange Sources -->
					<th  style="width:50%"  colspan="2">Blockchain.com</th>
				</tr>
				<tr style="width:100%;">
					<th id = "border" style="width:24.5%;"><strong>Sell:</strong></th><!-- Buy and Sell Price headers -->
					<th id = "border" style="width:24.5%;"><strong>Buy:</strong></th>
					<th id = "border" style="width:24.5%;"><strong>Sell:</strong></th>
					<th id = "border" style="width:24.5%;"><strong>Buy:</strong></th>
				</tr>
				<tr style="width:100%">
					<td id = "border" style="width:24.5%;color:{bsc1};">{bsell1}</td><!-- BTC/ETH buy/sell prices from source 1/2 -->
					<td id = "border" style="width:24.5%;color:{bbc1};">{bbuy1}</td>
					<td id = "border" style="width:24.5%;color:{bsc2};">{bsell2}</td>
					<td id = "border" style="width:24.5%;color:{bbc2};">{bbuy2}</td>
				</tr>
				<tr style="width:100%">
					<th style="width:25%"  colspan="4">Ethereum</th><!-- Coin Names -->
				</tr>
				<tr style="width:100%">
					<th style="width:50%"  colspan="2">Bitfinex.com</th>
					<th style="width:50%"  colspan="2">Kraken.com</th>
				</tr>
				<tr style="width:100%">
					<th id = "border" style="width:24.5%;"><strong>Sell:</strong></th>
					<th id = "border" style="width:24.5%;"><strong>Buy:</strong></th>
					<th id = "border" style="width:24.5%;"><strong>Sell:</strong></th>
					<th id = "border" style="width:24.5%;"><strong>Buy:</strong></th>
				</tr>
				<tr style="width:100%">
					<td id = "border" style="width:24.5%;color:{esc1};">{esell1}</td>
					<td id = "border" style="width:24.5%;color:{ebc1};">{ebuy1}</td>
					<td id = "border" style="width:24.5%;color:{esc2};">{esell2}</td>
					<td id = "border" style="width:24.5%;color:{ebc2};">{ebuy2}</td>
				</tr>
			</table>
		</part1>

		<part2>
			<h2><strong>Buy And Sell Recommendations</strong></h2><br>

			<table style="width:50%">
				<tr style="width:100%">
					<th style="width:100%"  colspan="4">Bitcoin</th><!-- Coin Names -->
				</tr>
				<tr style="width:100%">
					<th style="width:50%"  colspan="2">Buy:</th><!-- Recommend buy for both -->
					<th style="width:50%"  colspan="2">Sell:</th>
				</tr>
				<tr style="width:100%">
					<th id = "border" style="width:24.5%;"><strong>Source:</strong></th><!-- Exchange Sources/ price differences -->
					<th id = "border" style="width:24.5%;"><strong>Price Difference:</strong></th>
					<th id = "border" style="width:24.5%;"><strong>Source:</strong></th>
					<th id = "border" style="width:24.5%;"><strong>Price Difference:</strong></th>
				</tr>
				<tr style="width:100%">
					<td id = "border" style="width:24.5%;">{rbbuy}</td><!-- recommend Exchange Sources/ recommended price difference -->
					<td id = "border" style="width:24.5%;">{rbbd}</td>
					<td id = "border" style="width:24.5%;">{rbsell}</td>
					<td id = "border" style="width:24.5%">{rbsd}</td>

				</tr>
				<tr style="width:100%">
					<th style="width:100%"  colspan="4">Ethereum</th><!-- Coin Names -->
				</tr>
				<tr style="width:100%">
					<th style="width:50%"  colspan="2">Buy: </th>
					<th style="width:50%"  colspan="2">Sell: </th>
				</tr>
				<tr style="width:100%">
					<th id = "border" style="width:24.5%;"><strong>Source:</strong></th>
					<th id = "border" style="width:24.5%;"><strong>Price Difference:</strong></th>
					<th id = "border" style="width:24.5%;"><strong>Source:</strong></th>
					<th id = "border" style="width:24.5%;"><strong>Price Difference:</strong></th>
				</tr>
				<tr style="width:100%">
					<td id = "border" style="width:24.5%;">{rebuy}</td>
					<td id = "border" style="width:24.5%;">{rebd}</td>
					<td id = "border" style="width:24.5%;">{resell}</td>
					<td id = "border" style="width:24.5%;">{resd}</td>
				</tr>
			</table>
		</part2>
		{:catch error}
			<p style="color: red">{error.message}</p><!-- error message incase data can not be fetched -->
		{/await}
</main>

<style>
	:global(body) {/* set background color of entire page to beige */
		background-color: #FAEBD7;
	}
	table,tr,th,td{/* align table  */
		text-align: center;
		padding: 1em;
		margin: 0 auto;
	}
	th{/* set table header to blue */
		color:blue;
	}
	#border{/* set border to all elements with border id */
		color:blue;
		border-color:blue;
		border:solid;
		border-width:1px;
	}
	main {/* align main */
		text-align: center;
		padding: 1em;
		margin: 0 auto;
		width:100%;
	}
	h2{
		color:blue;
	}
	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>