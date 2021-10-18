import App from './App.svelte';//link to main app

const app = new App({//make new instace of app
	target: document.body,
	props: {
		name: 'BTC/ETH'//set name to coin names
	}
});

export default app;