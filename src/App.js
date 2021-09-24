import React from 'react';
import axios from 'axios';
import {Cards} from '../src/components/cards/cards';
import {BrowserRouter as Router , Route , Switch, Swtich} from 'react-router-dom';
class App extends React.Component {

	state = {
		details : [],
	}

	componentDidMount() {

		let data ;

		axios.get('http://127.0.0.1:8000/choosequiztype/')
		.then(res => {
			data = res.data;
			this.setState({
				details : data	
			});
			console.log('data:',data)
		})
		.catch(err => {})
	}

	render() {
		const details=this.state.details;
		
		return (
			<Router>
				<div className='App'>
					<Cards details={details}/>
				</div>
				<Switch>
					<Route exact path='/cont>
				</Route>
				<Route>
				</Route>
				</Switch>
				</Switch>
			</Router>

				  
		);
	}
}

export default App;
