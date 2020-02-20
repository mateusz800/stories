import React, { Fragment } from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";
import { withRouter } from "react-router-dom";
import styles from "./styles.module.css";
import { searchArticles } from "../../actions/articleActions";
import { Redirect } from "react-router";

class FilterColumn extends React.Component {
  constructor() {
    super();
    this.state = { search: "" };

    this.handleInputChange = this.handleInputChange.bind(this);
    this.handleSearchSubmit = this.handleSearchSubmit.bind(this);
  }
  handleInputChange(e) {
    this.setState({ search: e.target.value });
  }
  handleSearchSubmit() {
    const keywords = this.state.search;
    this.props.search(keywords);
    this.props.history.push(`/blog/search/${keywords}`);
  }
  render() {
    return (
      <Fragment>
        <div className={styles.container}>
          <form onSubmit={this.handleSearchSubmit}>
            <input
              type="search"
              placeholder="search"
              onChange={this.handleInputChange}
            />
          </form>
          <h5>New / Popular </h5>
        </div>
      </Fragment>
    );
  }
}

function mapDispatchToProps(dispatch) {
  return {
    search: keywords => dispatch(searchArticles(keywords))
  };
}

export default connect(null, mapDispatchToProps)(withRouter(FilterColumn));
